<script setup lang="ts">
definePageMeta({
  layout: "dashboard-layout",
  middleware: "auth",
});
</script>

<template>
  <div>
    <!-- <h3>Hola Mundo - Dashboard Page (Página Padre)</h3> -->
    <NuxtPage />
  </div>
</template>
