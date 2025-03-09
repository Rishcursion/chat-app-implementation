import { type Actions } from '@sveltejs/kit';
import { fail, redirect } from '@sveltejs/kit';

export const actions = {
	login: async ({ cookies, request }) => {
		const data = await request.formData();
		for (var pair of data.entries()) {
			console.log(pair[0] + ', ' + pair[1]);
		}
		const username = data.get('username');
		const password = data.get('password');
		const response = await fetch('http://localhost:8000/auth/login', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ username, password })
		});
		if (!response.ok) {
			return fail(400, { error: 'Uh Oh! Incorrect Credentials' });
		} else {
			const { access_token } = await response.json();
			cookies.set('Authorization', `Bearer ${access_token}`, {
				httpOnly: true,
				secure: true,
				sameSite: 'strict',
				path: '/'
			});
			throw redirect(303, '/home');
		}
	}
} satisfies Actions;
