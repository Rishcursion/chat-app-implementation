<script lang="ts">
	import { fly } from 'svelte/transition';
	import { linear, quartIn, elasticOut } from 'svelte/easing';
	import { onMount } from 'svelte';

	function typewriter(node, { speed = 50, delay = 0 }) {
		let text = node.textContent.trim();
		let index = 0;

		function update() {
			node.textContent = text.slice(0, index);
			if (index < text.length) {
				index++;
				setTimeout(update, speed);
			}
		}

		setTimeout(() => {
			node.textContent = ''; // Start with an empty element
			update();
		}, delay);

		return {
			destroy() {
				node.textContent = text; // Restore full text if unmounted
			}
		};
	}
	let isMounted = false;
	onMount(() => {
		isMounted = true;
	});
	function login_redirect() {
		window.location.href = '/auth/login';
	}
	function register_redirect() {
		window.location.href = '/auth/register';
	}
	const features = [
		{
			icon: '💬',
			title: 'Text Only Chats',
			description: 'Pure, distraction-free conversations for meaningful connections.'
		},
		{
			icon: '👥',
			title: 'Group Chats',
			description: 'Build communities and bring friends together in shared spaces.'
		},
		{
			icon: '⚡',
			title: 'Real-time Messaging',
			description: 'Stay connected with instant message delivery and typing indicators.'
		}
	];
</script>

<!-- card -->
{#if isMounted}
	<main class="flex min-h-screen items-center justify-center">
		<div
			class="flex w-4/5 flex-col items-center justify-center rounded-2xl border-2 border-black p-8"
			in:fly={{
				duration: 500,
				delay: 200,
				y: 400,
				easing: linear
			}}
		>
			<!-- About Section -->

			<div
				in:fly={{ duration: 1000, delay: 400, x: -200, easing: quartIn }}
				class="flex flex-col items-center justify-center text-center"
			>
				<!-- Title -->
				<div class="w-max">
					<h1
						use:typewriter={{ speed: 100 }}
						class="border-headline text-headline overflow-hidden border-r-4 text-5xl font-bold"
					>
						Textly
					</h1>
				</div>

				<!-- Tagline (Wrapped Multi-Line Typing Animation) -->
				<div class="flex w-max flex-col items-center justify-center">
					<p
						use:typewriter={{ speed: 50 }}
						class="text-paragraph text-center text-2xl leading-snug whitespace-pre-wrap"
					>
						Your personal minimalistic chat app to connect
					</p>
					<p
						use:typewriter={{ speed: 50, delay: 1200 }}
						class="text-paragraph w-max text-center text-2xl whitespace-pre-wrap"
					>
						with friends and family securely.
					</p>
				</div>
			</div>
			<!-- features section -->
			<div
				class="mt-16 grid grid-cols-1 gap-8 md:grid-cols-3"
				in:fly={{ duration: 800, delay: 1000, y: 50, easing: linear }}
			>
				{#each features as feature, i}
					<div
						class="hover:border-button transform rounded-lg bg-white/5 p-6 transition-all duration-500 hover:scale-105 hover:border-2"
						in:fly={{ duration: 500, delay: 1000 + i * 400, y: 50, easing: linear }}
					>
						<div class="mb-4 transform text-4xl transition-transform duration-500 hover:scale-110">
							{feature.icon}
						</div>
						<h3 class="text-headline text-3xl font-bold">{feature.title}</h3>
						<p class="text-paragraph mt-4 w-3/4 text-xl">{feature.description}</p>
					</div>
				{/each}
			</div>
			<!-- Account Setup Section -->
			<div class="flex flex-row items-center justify-between gap-x-12 pt-6">
				<button
					class="bg-button text-button-text hover:text-headline my-8 transform rounded-lg p-2 px-4 text-lg font-bold transition-all delay-100 ease-in hover:scale-105 active:scale-90"
					in:fly={{ duration: 500, delay: 1200, y: 50, easing: linear }}
					on:click={login_redirect}>Login!</button
				>
				<button
					class="bg-button text-button-text hover:text-headline my-8 transform rounded-lg p-2 text-lg font-bold transition-all delay-100 ease-in hover:scale-105 active:scale-90"
					in:fly={{ duration: 500, delay: 1200, y: 50, easing: linear }}
					on:click={register_redirect}>Register!</button
				>
			</div>
		</div>
	</main>
{/if}
