import { redirect, type Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	if (event.url.pathname.startsWith('/home') && !event.cookies.get('Authorization')) {
		throw redirect(401, '/');
	}
	const response = await resolve(event);
	return response;
};
