<script>
    import Navbar from '../components/navbar.svelte';
    import Content from '../components/content.svelte';

</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
:global(body){
    background-color: #fafafa;
    color: rgba(38, 38, 38, 0.7);
    font-family: "Lato",sans-serif;
    margin: 0;
    padding: 0;
}
:global(h1,h2,h3){
    margin: 0;
    padding: 0;
}
</style>

<Navbar></Navbar>
<Content></Content>