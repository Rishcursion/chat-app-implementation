import { type Actions } from '@sveltejs/kit';
import { fail, redirect } from '@sveltejs/kit';
import * as argon2 from 'argon2';

export const actions = {
	login: async ({ cookies, request }) => {
		const data = await request.formData();
		console.log('Login request recieved.');
		const username = data.get('username') as string;
		const password = data.get('password') as string;
		const hash_pass: string = await argon2.hash(password, {
			type: argon2.argon2id,
			hashLength: 16,
			parallelism: 1,
			memoryCost: 19,
			timeCost: 2
		});
	}
} satisfies Actions;
