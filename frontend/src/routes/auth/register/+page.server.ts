import { goto } from '$app/navigation';
import { json, type Actions } from '@sveltejs/kit';
import { fail, redirect } from '@sveltejs/kit';

export const actions = {
	register: async ({ cookies, request }) => {
		const data = await request.formData();
		const username = data.get('username') as string;
		const password = data.get('password') as string;
		const re_password = data.get('re_password') as string;
		if (re_password !== password) {
			return fail(400, { error: 'Passwords Do Not Match!!' });
		}
		const response = await fetch('http://localhost:8000/auth/register', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ username, password })
		});
		if (!response.ok) {
			const errorData = await response.json();
			return fail(response.status, { error: errorData.detail });
		} else {
			throw redirect(300, '/auth/login');
		}
	}
} satisfies Actions;
