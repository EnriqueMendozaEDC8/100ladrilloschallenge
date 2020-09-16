<script>
    import { onMount} from 'svelte';
    import Cart from 'svelte-material-icons/Cart.svelte';
    import { API_URI,CART } from '../store/store.js';
    import CardProperty from './cardProperty.svelte';
    let propertys = [];
    CART.update(r =>[]);
    onMount(async () =>{
        const response = await fetch(API_URI+'property/');
        let data = await response.json();
        propertys = data.propertys;
    });
</script>
  
<style>
</style>

{#each propertys as property}
<div class="container">
    <CardProperty
        id={property.id}
        name={property.name}
        location={property.location}
        detail={property.detail}
        highProfitability={property.highProfitability}
        lowProfitability={property.lowProfitability}
    />
</div>
{:else}
    <p>Loading ...</p>
{/each}