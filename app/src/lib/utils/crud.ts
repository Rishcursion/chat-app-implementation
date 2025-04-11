import { db } from './db';
import { type UserAuth } from 'kysely-codegen';

export async function get_login_details(username: string, password: string) {
	const result = db
		.selectFrom('user_auth')
		.selectAll()
		.where('user_name', '=', username)
		.executeTakeFirst();
	if (result === undefined) {
		return false;
	} else if (result.password === password) {
	}
}
