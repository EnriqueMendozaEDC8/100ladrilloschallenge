<script>
    export let id;
    export let name;
    export let location;
    export let detail;
    export let highProfitability;
    export let lowProfitability;

    import { readable, get } from 'svelte/store';
    import { CART, API_URI, USER } from '../store/store.js';

    let quantity = 1;
    async function addToCart() {
        let user = get(USER);
        console.log(user,id)
        const response = await fetch(API_URI + 'property/brick/' + id + '/');
        const brick = await response.json();
        let data = {
            quantity,
            idBroker:user.id,
            idBrick:brick.id
        }
        console.log(brick);
        await fetch(API_URI+'cart/add/',{
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

</script>

<style>
    .card-property{
        padding: 5px;
        background-color: darkslategrey;
        color: rgb(255, 255, 255);
        border-radius: 15px;
        margin-top: 15px;
    }

    .button-property{
        background: none;
        border: none;
    }
</style>

<button type="button" data-toggle="modal" data-target="#target{id}" class="button-property">
    <div class="row card-property">
        <div class="col">
            <h3>{name}</h3>
        </div>
        <div class="w-100"></div>
        <div class="col">{location}</div>
        <div class="w-100"></div>
        <div class="col">{detail}</div>
        <div class="w-100"></div>

        <div class="col">Rentabilidad:</div>
        <div class="col">{highProfitability}</div>
        <div class="col">{lowProfitability}</div>
    </div>
</button >

<div class="modal fade" id="target{id}" tabindex="-1" role="dialog" aria-labelledby="target{id}Label" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="target{id}Label">{name}</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body row">
                <div class="w-100"></div>
                <div class="col">{location}</div>
                <div class="w-100"></div>
                <div class="col">{detail}</div>
                
                <div class="w-100"></div>
                <div class="col">Rentabilidad:</div>
                <div class="col">{highProfitability}</div>
                <div class="col">{lowProfitability}</div>
                
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <input value={quantity} type="number">
                <button type="button" class="btn btn-primary" on:click={addToCart}>Add</button>
            </div>
        </div>
    </div>
</div>