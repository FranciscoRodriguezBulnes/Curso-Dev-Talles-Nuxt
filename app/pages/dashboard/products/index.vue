<template>
  <div class="space-y-6">
    <!-- Header with Action Button -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-gray-900 dark:text-white">
          Productos
        </h1>
        <p class="text-gray-600 dark:text-gray-400 mt-2">
          Gestiona y organiza tu catálogo de productos
        </p>
      </div>
      <UButton
        to="/dashboard/product/new"
        icon="i-lucide-plus"
        label="Agregar Producto"
        color="primary"
        size="lg"
      />
    </div>

    <UTable
      :data="products"
      :columns="columns"
      class="flex-1"
    />

    <SharedPagination
      :total="total"
      :model-value="currentPage"
      :per-page="perPage"
    />
  </div>
</template>

<script setup lang="ts">
import { h, resolveComponent } from "vue";
import type { TableColumn } from "@nuxt/ui";
const UBadge = resolveComponent("UBadge");
const NuxtLink = resolveComponent("NuxtLink");
// type Payment = {
//   id: string;
//   date: string;
//   status: "paid" | "failed" | "refunded";
//   email: string;
//   amount: number;
// };

const { products, currentPage, perPage, total } = await usePaginatedProducts();

const columns: TableColumn<Product>[] = [
  {
    accessorKey: "id",
    header: "#",
    cell: ({ row }) => `#${row.getValue("id")}`,
  },

  //Image

  {
    accessorKey: "images",
    header: "Imagen",
    cell: ({ row }) => {
      const images = row.getValue("images") as string[];
      const url = Array.isArray(images) && images.length > 0 ? images[0] : "";
      // const url = images[0] ?? "";

      if (!url) return h("span", { class: "text-gray-500" }, "sin imagen");

      return h("img", {
        src: url,
        alt: "Imagen del producto",
        style:
          "with: 48px; height:48px; object-fit:cover; border-radius:0.5 rem",
      });
    },
  },

  {
    accessorKey: "name",
    header: "Nombre",
    cell: ({ row }) => {
      const productId = row.getValue("id");
      const productName = row.getValue("name");

      return h(
        NuxtLink,
        {
          to: `/dashboard/product/${productId}`,
          class: "text-indigo-500 hover:text-blue-700 underline cursor-pointer",
        },

        () => productName,
      );
    },
  },
  {
    accessorKey: "description",
    header: "Descripción",
    cell: ({ row }) => {
      return h(
        "div",
        {
          style:
            "white-space:normal; word-breack: breack-word; max-width:300px",
          class: "truncate-text",
        },
        String(row.getValue("description")).slice(0, 50) + " ...",
      );
    },
  },

  {
    accessorKey: "tags",
    header: "Etiquetas",
    cell: ({ row }) => {
      const tags = row.getValue("tags") as string[];
      if (!Array.isArray(tags)) return "";

      return h(
        "div",
        { class: "flex flex-wrap, gap-1" },
        tags.map((tag) =>
          h(
            UBadge,
            {
              size: "xs",
              color: "primary",
              variant: "subtle",
              class: "mr-0.5",
            },
            () => tag,
          ),
        ),
      );
    },
  },
  {
    accessorKey: "price",
    header: "Precio",
    cell: ({ row }) => formatCurrency(row.getValue("price")),
  },

  {
    accessorKey: "createdAt",
    header: "Creado",
    cell: ({ row }) => {
      const value = row.getValue("createdAt");
      return value ? dayMonthYearFormat(new Date(value as string)) : "";
    },
  },
];
</script>
