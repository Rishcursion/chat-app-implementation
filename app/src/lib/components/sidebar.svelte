<script lang="ts">
	import ChatList from './chat_list.svelte';
	import { current_user, chatting_with } from '$lib/store/globalState';
	type test = {
		chat_id: number;
		username: string;
		timestamp: string;
		message_head: string;
		messages: {
			content: string;
			sender: string;
			time: string;
		}[];
	};
	let {
		username,
		invite_code,
		user_data
	}: { username: string; invite_code: string; user_data: test[] } = $props();
	let search_term: string = $state('');
	let active_tab: string = $state('chat');
	let filtered_chats = $derived(
		user_data.filter((chat: any) => chat.username.toLowerCase().includes(search_term.toLowerCase()))
	);
</script>

<!-- sidebar -->
<aside class="flex h-screen w-1/5 flex-col bg-white/10 backdrop-blur-lg lg:relative">
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
	<!-- Chat Type Selection -->
	<div class="mb-8 flex w-full flex-row items-center justify-center pt-4">
		<button
			class="{active_tab == 'chat'
				? 'bg-illustration-highlight text-button-text'
				: 'bg-illustration-main'} border-r-illustration-stroke ml-2 w-4/6 rounded-l-md
				border-r-2 px-3 py-2 transition-colors ease-in"
			onclick={() => {
				active_tab = 'chat';
			}}>Chats</button
		>
		<button
			class="{active_tab == 'group'
				? 'bg-illustration-highlight text-button-text'
				: 'bg-illustration-main'} mr-2 w-4/6 rounded-r-md p-2 transition-colors ease-in"
			onclick={() => {
				active_tab = 'group';
			}}>Groups</button
		>
	</div>
	<!-- Search Bar -->
	<div class="flex flex-row items-center justify-center pb-4">
		<img src="/search.svg" class="w-8 pr-2" alt="search for specific chats" />
		<input
			type="text"
			name="chat_search"
			class="text-paragraph border-illustration-main w-max rounded-md border-1 p-2 outline-0"
			placeholder="Search Active Chats"
			bind:value={search_term}
		/>
	</div>
	<div class="flex grow flex-col overflow-y-auto">
		{#if active_tab === 'chat'}
			<!-- Message Tab -->
			{#if filtered_chats.length === 0}
				<p class="text-paragraph ml-4">No results matching that search term found :(</p>
			{:else}
				{#each filtered_chats as data}
					<!-- content here -->
					<button
						onclick={() => {
							chatting_with.set(data.chat_id);
						}}
						onkeydown={() => {
							chatting_with.set(data.chat_id);
						}}
					>
						<ChatList
							username={data.username}
							timestamp={data.timestamp}
							message_head={data.message_head}
							is_active={data.chat_id === $chatting_with}
						/>
					</button>
				{/each}{/if}
		{:else}
			<!-- else content here -->
		{/if}
	</div>
</aside>
