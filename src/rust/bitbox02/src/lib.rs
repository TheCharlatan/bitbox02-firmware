// Copyright 2019 Shift Cryptosecurity AG
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// This crate contains safe wrappers around C functions provided by bitbox02_sys.
#![no_std]

use bitbox02_sys::{self, delay_ms, delay_us};
use core::time::Duration;

pub fn ug_put_string(x: i16, y: i16, input: &str, inverted: bool) {
    // rust strings (&str) are not null-terminated, ensure that there always is a \0 byte.
    let len = core::cmp::min(127, input.len());
    let mut buf = [0u8; 128];
    let buf = &mut buf[0..len];
    let input = &input.as_bytes()[0..len];
    buf.copy_from_slice(input);
    unsafe { bitbox02_sys::UG_PutString(x, y, buf.as_ptr() as *const _, inverted) }
}

pub fn ug_clear_buffer() {
    unsafe { bitbox02_sys::UG_ClearBuffer() }
}

pub fn ug_send_buffer() {
    unsafe { bitbox02_sys::UG_SendBuffer() }
}

pub fn ug_font_select() {
    unsafe { bitbox02_sys::UG_FontSelect(&bitbox02_sys::font_font_a_9X9) }
}

pub fn delay(duration: Duration) {
    if duration < Duration::from_micros(1) {
        unsafe {
            // Sleep the smallest unit of sleep we support
            delay_us(1)
        }
    } else if duration < Duration::from_millis(1) {
        unsafe {
            delay_us(duration.as_micros() as u16);
        }
    } else {
        unsafe {
            delay_ms(duration.as_millis() as u16);
        }
    }
}

// Safe wrapper for workflow_confirm
pub fn workflow_confirm(title: &str, body: &str, longtouch: bool, accept_only: bool) -> bool {
    // Ensure valid nullterminated C-str
    // Will truncate title if it is too long
    let title_cstr = {
        const TITLE_LEN: usize = 20;
        let len = core::cmp::min(TITLE_LEN, title.len());
        let mut buf = [0u8; TITLE_LEN + 1];
        // resize title to actual length
        let title = &title.as_bytes()[0..len];
        // copy from title to buf
        buf[0..len].copy_from_slice(title);
        buf
    };
    // same as title_cstr
    let body_cstr = {
        const BODY_LEN: usize = 100;
        let len = core::cmp::min(BODY_LEN, body.len());
        let mut buf = [0u8; BODY_LEN + 1];
        // resize body to actual length
        let body = &body.as_bytes()[0..len];
        // copy from body to buf
        buf[0..len].copy_from_slice(body);
        buf
    };

    unsafe {
        bitbox02_sys::workflow_confirm(
            title_cstr.as_ptr() as *const _,
            body_cstr.as_ptr() as *const _,
            longtouch,
            accept_only,
        )
    }
}
