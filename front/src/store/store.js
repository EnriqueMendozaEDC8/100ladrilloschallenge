  
import { writable } from 'svelte/store';

export const LOG_IN = writable(0);

export const CART = writable(localStorage.getItem("cart"));

export const USER = writable(localStorage.getItem("user"));
export const API_URI = 'http://127.0.0.1:8000/api/';

