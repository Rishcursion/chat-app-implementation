--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;


--
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: direct_messages; Type: TABLE; Schema: public; Owner: dev
--

CREATE TABLE public.direct_messages (
    message_id bigint NOT NULL,
    reciever_id integer
);


ALTER TABLE public.direct_messages OWNER TO dev;

--
-- Name: group_info; Type: TABLE; Schema: public; Owner: dev
--

CREATE TABLE public.group_info (
    group_id integer NOT NULL,
    created_by integer,
    created_on timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    last_active timestamp without time zone,
    invite_code bytea,
    description text,
    group_name text NOT NULL,
    member_count integer DEFAULT 1,
    isprivate boolean DEFAULT true,
    isdeleted boolean DEFAULT false
);


ALTER TABLE public.group_info OWNER TO dev;

--
-- Name: group_info_group_id_seq; Type: SEQUENCE; Schema: public; Owner: dev
--

CREATE SEQUENCE public.group_info_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.group_info_group_id_seq OWNER TO dev;

--
-- Name: group_info_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dev
--

ALTER SEQUENCE public.group_info_group_id_seq OWNED BY public.group_info.group_id;


--
-- Name: group_members; Type: TABLE; Schema: public; Owner: dev
--

CREATE TABLE public.group_members (
    group_id integer NOT NULL,
    member_id integer,
    member_role character varying(5)
);


ALTER TABLE public.group_members OWNER TO dev;

--
-- Name: group_messages; Type: TABLE; Schema: public; Owner: dev
--

CREATE TABLE public.group_messages (
    message_id bigint NOT NULL,
    group_id integer
);


ALTER TABLE public.group_messages OWNER TO dev;

--
-- Name: user_auth; Type: TABLE; Schema: public; Owner: dev
--

CREATE TABLE public.user_auth (
    user_id integer NOT NULL,
    user_name character varying(64) NOT NULL,
    password character(73) NOT NULL,
    bio text,
    friend_code bytea DEFAULT public.gen_random_bytes(4),
    created_on timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.user_auth OWNER TO dev;

--
-- Name: user_auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: dev
--

CREATE SEQUENCE public.user_auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_auth_user_id_seq OWNER TO dev;

--
-- Name: user_auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dev
--

ALTER SEQUENCE public.user_auth_user_id_seq OWNED BY public.user_auth.user_id;


--
-- Name: user_messages; Type: TABLE; Schema: public; Owner: dev
--

CREATE TABLE public.user_messages (
    message_id bigint NOT NULL,
    sender_id integer NOT NULL,
    sent_time timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    message_content text NOT NULL,
    reply_to bigint,
    read_reciepts jsonb,
    edited_time timestamp without time zone,
    isdeleted boolean DEFAULT false,
    edited boolean DEFAULT false
);


ALTER TABLE public.user_messages OWNER TO dev;

--
-- Name: user_messages_message_id_seq; Type: SEQUENCE; Schema: public; Owner: dev
--

CREATE SEQUENCE public.user_messages_message_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_messages_message_id_seq OWNER TO dev;

--
-- Name: user_messages_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dev
--

ALTER SEQUENCE public.user_messages_message_id_seq OWNED BY public.user_messages.message_id;


--
-- Name: group_info group_id; Type: DEFAULT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.group_info ALTER COLUMN group_id SET DEFAULT nextval('public.group_info_group_id_seq'::regclass);


--
-- Name: user_auth user_id; Type: DEFAULT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.user_auth ALTER COLUMN user_id SET DEFAULT nextval('public.user_auth_user_id_seq'::regclass);


--
-- Name: user_messages message_id; Type: DEFAULT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.user_messages ALTER COLUMN message_id SET DEFAULT nextval('public.user_messages_message_id_seq'::regclass);


--
-- Name: direct_messages direct_messages_pkey; Type: CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.direct_messages
    ADD CONSTRAINT direct_messages_pkey PRIMARY KEY (message_id);


--
-- Name: group_info group_info_pkey; Type: CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.group_info
    ADD CONSTRAINT group_info_pkey PRIMARY KEY (group_id);


--
-- Name: group_members group_members_pkey; Type: CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.group_members
    ADD CONSTRAINT group_members_pkey PRIMARY KEY (group_id);


--
-- Name: group_messages group_messages_pkey; Type: CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.group_messages
    ADD CONSTRAINT group_messages_pkey PRIMARY KEY (message_id);


--
-- Name: user_auth user_auth_pkey; Type: CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.user_auth
    ADD CONSTRAINT user_auth_pkey PRIMARY KEY (user_id);


--
-- Name: user_messages user_messages_pkey; Type: CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.user_messages
    ADD CONSTRAINT user_messages_pkey PRIMARY KEY (message_id);


--
-- Name: direct_messages direct_messages_message_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.direct_messages
    ADD CONSTRAINT direct_messages_message_id_fkey FOREIGN KEY (message_id) REFERENCES public.user_messages(message_id);


--
-- Name: direct_messages direct_messages_reciever_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.direct_messages
    ADD CONSTRAINT direct_messages_reciever_id_fkey FOREIGN KEY (reciever_id) REFERENCES public.user_auth(user_id);


--
-- Name: group_info group_info_created_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.group_info
    ADD CONSTRAINT group_info_created_by_fkey FOREIGN KEY (created_by) REFERENCES public.user_auth(user_id);


--
-- Name: group_members group_members_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.group_members
    ADD CONSTRAINT group_members_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.group_info(group_id);


--
-- Name: group_members group_members_member_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.group_members
    ADD CONSTRAINT group_members_member_id_fkey FOREIGN KEY (member_id) REFERENCES public.user_auth(user_id);


--
-- Name: group_messages group_messages_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.group_messages
    ADD CONSTRAINT group_messages_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.group_info(group_id);


--
-- Name: group_messages group_messages_message_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.group_messages
    ADD CONSTRAINT group_messages_message_id_fkey FOREIGN KEY (message_id) REFERENCES public.user_messages(message_id);


--
-- Name: user_messages user_messages_reply_to_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.user_messages
    ADD CONSTRAINT user_messages_reply_to_fkey FOREIGN KEY (reply_to) REFERENCES public.user_messages(message_id);


--
-- Name: user_messages user_messages_sender_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dev
--

ALTER TABLE ONLY public.user_messages
    ADD CONSTRAINT user_messages_sender_id_fkey FOREIGN KEY (sender_id) REFERENCES public.user_auth(user_id);


--
-- PostgreSQL database dump complete
--

