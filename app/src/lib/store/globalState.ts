import { writable, type Writable, derived } from 'svelte/store';

export const current_user: Writable<number> = writable<number>(-1);
export const chatting_with: Writable<number> = writable<number>(-1);
export const isTyping: Writable<boolean> = writable<boolean>(false);
export const userTyping: Writable<boolean> = writable<boolean>(false);
