<template>
    <b-navbar toggleable type="dark" variant="dark fixed-top">
            <b-navbar-brand href="/"><img alt="Vue logo" class="nav-logo" src="../../assets/logo.png"></b-navbar-brand>

            <b-navbar-toggle target="navbar-toggle-collapse" style="border-color: transparent !important; box-shadow: none !important;">
                <template #default="{ expanded }">
                    <b-icon v-if="expanded" icon="chevron-compact-up"></b-icon>
                    <b-icon v-else icon="chevron-compact-down"></b-icon>
                </template>
            </b-navbar-toggle>

            <b-collapse id="navbar-toggle-collapse" is-nav>
                <b-navbar-nav class="ml-auto">
                    <b-nav-item href="/about">About me</b-nav-item>
                    <b-nav-item href="/profile">Profiles</b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
</template>

<script>
export default {

}
</script>

<style>
.nav-logo{
    width:120px;
}
.ml-auto{
    padding-left: 25px !important;
}

</style>