<script>
    export let broker;
    export let brick;
    import { USER, API_URI, CART } from '../store/store.js';
    import { readable, get } from 'svelte/store';
    
    async function remove() {
        const response = await fetch(API_URI+'cart/delete/',{
            method: 'POST',
            body: JSON.stringify({"idBroker":broker,"idBrick":brick})
        });
        const content = await response.json();
        console.log(content);
    }
</script>

<style>

</style>

<div class="col">
    <button type="button" class="btn btn-danger" on:click={remove}> Remover </button>
</div>