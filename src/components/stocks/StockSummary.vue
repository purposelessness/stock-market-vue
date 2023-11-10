<script setup lang="ts">

import type {StockImprint} from "@/types/stockImprint";

const payload = defineProps<{ stockImprint: StockImprint }>();

</script>

<template>

  <div class="stock-summary">
    <p>Price: {{ payload.stockImprint.price ?? 'None' }}</p>
    <p>Quantity: {{ payload.stockImprint.quantity }}</p>
  </div>

</template>

<style scoped>

</style>