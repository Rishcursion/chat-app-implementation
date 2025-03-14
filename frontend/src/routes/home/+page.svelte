<script lang="ts">
	import { onMount } from 'svelte';
	import { quintIn } from 'svelte/easing';
	import { fly } from 'svelte/transition';
	import ChatWindow from '$lib/components/chat_window.svelte';
	type UserData = {
		username: string;
		invite_code: string;
	};
	type test = {
		username: string;
		timestamp: string;
		message_head: string;
	};
	let { data }: { user?: UserData } = $props();
	// User Details
	let username: string = data.user.username;
	let invite_code: string = data.user.invite_code;
	// App State Related Details
	let search_term: string = $state('');
	let active_tab: string = $state('chat');
	//Test data
	const test_data: test[] = [
		{
			username: 'John',
			timestamp: '21:44',
			message_head: 'i want to fuk.'
		},

		{
			username: 'Lily',
			timestamp: '21:44',
			message_head: 'i want to meet.'
		},
		{
			username: 'dumass',
			timestamp: '21:45',
			message_head: 'man this is boring.'
		}
	];
</script>

<main class="bg-background min-h-screen min-w-screen">
	<!-- sidebar -->
	<aside class="fixed flex h-screen w-1/5 flex-col bg-white/10 backdrop-blur-lg lg:relative">
		<div class="space-y-4 p-4">
			<!-- User Profile -->
			<div
				class="flex flex-col items-center justify-center rounded-lg bg-white/5 p-4 backdrop-blur-lg"
			>
				<div
					class="bg-illustration-highlight flex h-16 w-16 shrink grow-0 items-center justify-center rounded-full text-xl"
				>
					{username.charAt(0).toUpperCase()}
				</div>
				<p class="text-paragraph pt-2 text-xl font-semibold">{username}</p>
				<button
					class="text-illustration-highlight hover:text-illustration-main transform font-medium transition-all ease-in hover:scale-105 active:scale-95"
				>
					@{invite_code}
				</button>
			</div>
		</div>
		<!-- Search Bar -->
		<div class="flex flex-row items-center justify-center">
			<img src="/search.svg" class="w-8 pr-2" alt="search for specific chats" />
			<input
				type="text"
				name="chat_search"
				class="text-paragraph border-illustration-main w-max rounded-md border-1 p-2 outline-0"
				placeholder="Search Active Chats"
				bind:value={search_term}
			/>
		</div>
		<!-- Chat Type Selection -->
		<div class="mb-8 flex w-full flex-row items-center justify-center pt-4">
			<button
				class="{active_tab == 'chat'
					? 'bg-illustration-highlight text-button-text'
					: 'bg-illustration-main'} border-r-illustration-stroke rounded-l-md border-r-2
				px-3 py-2 transition-colors ease-in"
				onclick={() => {
					active_tab = 'chat';
				}}>Chats</button
			>
			<button
				class="{active_tab == 'group'
					? 'bg-illustration-highlight text-button-text'
					: 'bg-illustration-main'} rounded-r-md p-2 transition-colors ease-in"
				onclick={() => {
					active_tab = 'group';
				}}>Groups</button
			>
		</div>
		{#if active_tab === 'chat'}
			<!-- Message Tab -->
			{#each test_data as data, i}
				<!-- content here -->
				<ChatWindow
					username={data.username}
					timestamp={data.timestamp}
					message_head={data.message_head}
					idx={i}
				/>
			{/each}
		{:else}
			<!-- else content here -->
		{/if}
	</aside>
</main>
