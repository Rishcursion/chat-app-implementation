import { error, redirect } from '@sveltejs/kit';
import { type Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { chatting_with, isTyping, socket } from '$lib/store/globalState';
import { derived, get } from 'svelte/store';
export const load: PageServerLoad = async ({ fetch, cookies }) => {
	const token = cookies.get('Authorization');
	if (!token) {
		return null;
	}
	const response = await fetch('http://localhost:8000/auth/me', {
		method: 'GET',
		headers: { 'Content-Type': 'application/json', Authorization: `${token}` }
	});
	if (!response.ok) {
		throw error(401, 'Token Expired Or Invalid');
	}
	const user = await response.json();
	return { user };
};
export const actions = {
	dispose_stale_cookies: async ({ cookies }) => {
		cookies.delete('Authorization', { path: '/' });
		throw redirect(301, '/auth/login');
	},
	send_message: async ({ request }) => {
		const data = await request.formData();
		let message_content = data.get('send-message') as string;
		let reciever_id = data.get('reciever') as number;
		if (message_content === '') {
			throw error(400, 'Message Content Cannot Be Empty!');
		} else if (reciever_id === -1) {
			throw error(400, 'Invalid User');
		} else {
			socket.emit('message_event', {
				reciever: reciever_id,
				content: message_content
			});
		}
	}
} satisfies Actions;

socket.on('connect', () => {
	console.log('Connected To Server Websocket');
});
socket.on('disconnect', () => {
	console.log('Disconnected To Server Websocket');
});

socket.on('sender_typing_status', (data: { user_id: number; isTyping: boolean }) => {
	console.log(`[Frontend] Received typing update:`, data);
	isTyping.set(data['isTyping']);
});
socket.on('new_message', (data: { content: string }) => {
	console.log('Recieved New Message: ', data.content);
});
socket.connect();
