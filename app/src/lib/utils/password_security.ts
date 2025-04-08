import * as argon2 from 'argon2';
export async function hash_password(input_pass: string) {
	const hashed_password = await argon2.hash(input_pass, {
		type: argon2.argon2id,
		memoryCost: 2 ** 16,
		hashLength: 50
	});
}
