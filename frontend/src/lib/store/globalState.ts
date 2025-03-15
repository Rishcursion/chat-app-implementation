import { writable } from 'svelte/store';

// Create a store to track the active chat
export const activeChat = writable<number>(-1);
