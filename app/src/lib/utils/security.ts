import * as jose from 'jose';
export async function gen_key(username: string, user_id: number) {
	const jwt = new jose.SignJWT({ id: user_id, username: username })
		.setProtectedHeader({
			alg: 'RS256'
		})
		.setIssuer('textly.org')
		.setIssuedAt(Date())
		.setExpirationTime(import.meta.env.JWT_EXPIRATION_TIME)
		.sign(import.meta.env.JWT_SECRET);
}
