// env.d.ts
/// <reference types="vite/client" />

interface ImportMetaEnv {
	readonly DB_NAME: string;
	readonly DB_PORT: string;
	readonly DB_SERVER: string;
	readonly DB_USER: string;
	readonly DB_PASSWORD: string;
	readonly DATABASE_URL: string;
	readonly JWT_EXPIRATION_TIME: string;
	readonly JWT_SECRET: string;

	// Optional: expose to client (must start with PUBLIC_)
	// readonly PUBLIC_API_URL: string;
}

interface ImportMeta {
	readonly env: ImportMetaEnv;
}
