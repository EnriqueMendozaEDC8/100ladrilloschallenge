<script>
    import Cart from "svelte-material-icons/Cart.svelte";
    import Remove from "./remove.svelte";
    import { USER, API_URI, CART } from '../store/store.js';
    import { readable, get } from 'svelte/store';
    let email = "enrique.510.06@gmail.com";
    let user = get(USER);

    let data = {};
    let items = [];

    let cartInformation = "block";
    let cartNotice = "none";
    let cartPay = "none";

    async function login() {
        const response = await fetch(API_URI+'broker/',{
            method: 'POST',
            body: JSON.stringify({"email":"enrique.510.06@gmail.com"})
        });
        const content = await response.json();
        USER.set(content);
        user = get(USER);
    }

    async function cart(){
        let user = get(USER);
        const cart = await fetch(API_URI + 'cart/' + user.id + '/');
        data = await cart.json();
        items = data.items;
        console.log(data);
    }

    function cartContinueToNotice() {
        cartNotice = "block";
        cartInformation = "none";
    }
    
    function cartContinueToEndShop() {
        cartPay = "block";
        cartNotice = "none";
    }
    
    async function cartEndShop() {
        const response = await fetch(API_URI+'cart/checkout/',{
            method: 'POST',
            body: JSON.stringify({"idBroker":user.id})
        });
        const content = await response.json();
        console.log(content);

        cartInformation = "block";
        cartPay = "none";
    }
</script>
  
<style>
    .button-cart{
        background: none;
        border:none;
    }
</style>
  
<div class="Navbar">
    <nav class="navbar navbar-dark bg-dark">
        <a class="navbar-brand" href="">
            Challengue 100 Ladrillos
        </a>
        {#if user != null}
            <button class="button-cart" on:click={cart} data-toggle="modal" data-target="#cartModal">
                <Cart color={"#ffffff"} width={25} height={25}/>
            </button>
            
        {:else}
            <span>
                <div class="input-group">
                    <div class="input-group-prepend">
                        <button class="btn btn-outline-secondary" type="button" on:click={login}>Entrar</button>
                    </div>
                    <input value={email} type="text" class="form-control" placeholder="" aria-label="" aria-describedby="basic-addon1">
                </div>
            </span>
        {/if}
    </nav>
</div>

<div class="modal fade" id="cartModal" tabindex="-1" role="dialog" aria-labelledby="targetcartLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="cartLabel">Carrito</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body row">
                {#if cartInformation!= "none" || cartPay!= "none"}
                    <div class="col">
                        <h3>{data.name}</h3>
                    </div>
                    <div class="w-100"></div>
                    {#each items as item}
                        <div class="col">
                            <h6>{item.property}</h6>
                        </div>
                        <div class="col">
                            <h6>{item.quantity}</h6>
                        </div>
                        <div class="col">
                            <h6>{item.price}</h6>
                        </div>
                        {#if cartInformation!= "none"}
                            <Remove brick={item.brickId} broker={user.id}/>
                        {/if}
                        <div class="w-100"></div>
                    {/each}
                    <div class="col">
                        <h6>Total:</h6>
                    </div>
                    <div class="col">
                        <h6>{data.total}</h6>
                    </div>
                {/if}
                
                {#if cartNotice!= "none"}
                    <div class="col">
                        <h3>Aviso</h3>
                    </div>
                    <div class="w-100"></div>
                    <div class="col">
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                    </div>
                {/if}
                
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" style="display:{cartInformation};" on:click={cartContinueToNotice}>Continuar</button>
                <button type="button" class="btn btn-primary" style="display:{cartNotice};" on:click={cartContinueToEndShop}>Aceptar</button>
                <button type="button" class="btn btn-primary" style="display:{cartPay};" on:click={cartEndShop}>Finalizar compra</button>
            </div>
        </div>
    </div>
</div>