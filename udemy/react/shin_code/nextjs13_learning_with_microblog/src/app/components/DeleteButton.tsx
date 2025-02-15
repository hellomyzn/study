"use client";
import { deleteArticle } from "@/blogAPI";
import { useRouter } from "next/navigation";
import React from "react";

const DeleteButton = ({ id }: { id: string }) => {
  const router = useRouter();
  const handleDelete = async () => {
    // await deleteArticle(id);

    const API_URL = process.env.NEXT_PUBLIC_API_URL;
    await fetch(`${API_URL}/api/blog/${id}`, {
      method: "DELETE",
    });

    router.push("/");
    router.refresh();
  };
  return (
    <div
      onClick={handleDelete}
      className="bg-red-500 hover:bg-red-600 rounded-md py-2 px-5 inline cursor-pointer"
    >
      Delete
    </div>
  );
};

export default DeleteButton;
