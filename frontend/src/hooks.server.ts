import { redirect, type Handle } from '@sveltejs/kit';
const valid_paths = new Set(['/home', '/auth/login', '/auth/register', '/']);
const user_paths = new Set(['/auth/login', '/auth/register']);
export const handle: Handle = async ({ event, resolve }) => {
	if (event.url.pathname.startsWith('/home') && !event.cookies.get('Authorization')) {
		throw redirect(401, '/');
	} else if (!valid_paths.has(event.url.pathname)) throw redirect(404, '/');
	else if (user_paths.has(event.url.pathname) && event.cookies.get('Authorization'))
		throw redirect(302, '/home');
	const response = await resolve(event);
	return response;
};
