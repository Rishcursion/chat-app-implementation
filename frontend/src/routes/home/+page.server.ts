import { error, redirect } from '@sveltejs/kit';
import { type Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
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
	console.log(user);
	return { user };
};
export const actions = {
	dispose_stale_cookies: async ({ cookies }) => {
		cookies.delete('Authorization', { path: '/' });
		throw redirect(301, '/auth/login');
	}
} satisfies Actions;
