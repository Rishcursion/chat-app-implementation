<script lang="ts">
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
	let message_search_term: string = $state('');
	let {user_data, active_chat}:{user_data:test[],active_chat:number} = $props()
	let active_username = $derived(user_data.find((chat) => chat.chat_id === active_chat)?.username);
	// **Computed Filtered List**
	// the user_data will be replaced with the retrieved messages from the server
	let active_chat_obj = $derived(user_data.find((chat) => chat.chat_id === active_chat));
	let filtered_message = $derived(
		active_chat_obj?.messages.filter((msg) =>
			msg.content.toLowerCase().includes(message_search_term.toLowerCase())
		)
	);
	function get_initials(username: string) {
		let components = username.split(' ');

		if (components.length > 1) {
			return (
				(components.at(0)?.at(0)?.toUpperCase() || '') +
				(components.at(1)?.at(0)?.toUpperCase() || '')
			);
		} else {
			return components.at(0)?.at(0)?.toUpperCase() || '';
		}
	}
</script>
		<div class="flex h-screen w-4/5 flex-col backdrop-blur-md transition-colors delay-100 ease-in">
			<nav class="bg-background fixed top-0 flex h-1/6 w-full items-center justify-between">
				<div
					class="bg-button ml-4 flex h-16 w-16 flex-row items-center justify-center rounded-full text-2xl font-bold"
				>
					{get_initials(active_username || '')}
				</div>
				<p class="text-headline ml-4 text-3xl font-semibold">{active_username}</p>
				<div class="mr-4 flex flex-row items-center justify-center">
					<img src="/search.svg" class="w-8 pr-2" alt="search for messages" />
					<input
						type="text"
						name="message_search"
						class="text-paragraph border-illustration-main w-max rounded-md border-1 p-2 outline-0"
						placeholder="Search Messages"
						bind:value={message_search_term}
					/>
				</div>
			</nav>
			<!-- Chat Window -->
			<div class="flex grow flex-col space-y-4 overflow-y-auto p-6 pt-[18vh]">
				<!-- Messages -->
				{#each filtered_message || [] as message}
					<div class={`flex ${message.sender === 'You' ? 'justify-end' : 'justify-start'}`}>
						<div
							class={`max-w-[70%] rounded-lg px-4 py-2 ${
								message.sender === 'You'
									? 'bg-button text-button-text'
									: 'bg-illustration-stroke text-paragraph'
							}`}
						>
							<div class="text-sm">{message.content}</div>
							<div class="mt-1 text-xs opacity-70">{message.time}</div>
						</div>
					</div>
				{/each}
			</div>
			<!-- Send Message Section -->
			<div
				class="bg-illustration-main/30 flex h-16 w-full flex-row items-center justify-center backdrop-blur-lg"
			>
				<input
					type="text"
					class="bg-background/40 text-paragraph focus:border-illustration-main m-4 w-full rounded-lg p-2 py-2 outline-0 focus:border-2"
					placeholder="Start Typing..."
					autocorrect="on"
					name="send-message"
				/>
				<button type="submit" class="items-center justify-center">
					<img
						src="/send.svg"
						class="mr-4 mb-2 w-12 active:scale-105"
						alt="Send Typed Message"
					/></button
				>
			</div>
		</div>
