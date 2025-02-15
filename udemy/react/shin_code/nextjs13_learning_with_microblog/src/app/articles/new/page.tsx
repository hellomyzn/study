"use client";

import { createArticle } from "@/blogAPI";
import { useRouter } from "next/navigation";
import React, { useState } from "react";

const CreateBlogPage = () => {
  const API_URL = process.env.NEXT_PUBLIC_API_URL;

  const [id, setId] = useState<string>("");
  const [title, setTitle] = useState<string>("");
  const [content, setContent] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    // await createArticle(id, title, content);

    await fetch(`${API_URL}/api/blog`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id, title, content }),
    });
    setLoading(false);

    router.push("/");
    router.refresh();
  };
  return (
    <div className="min-h-screen py-8 px-4 md:px-12">
      <h2 className="text-2xl font-bold mb-4">new article</h2>
      <form
        onSubmit={handleSubmit}
        action=""
        className="bg-slate-200 p-6 rounded shadow-lg"
      >
        <div className="mb-4">
          <label htmlFor="" className="text-gray-700 text-sm font-bold mb-2">
            URL
          </label>
          <input
            type="text"
            onChange={(e) => setId(e.target.value)}
            className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none"
          />
        </div>
        <div className="mb-4">
          <label htmlFor="" className="text-gray-700 text-sm font-bold mb-2">
            Title
          </label>
          <input
            type="text"
            onChange={(e) => setTitle(e.target.value)}
            className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none"
          />
        </div>
        <div className="mb-4">
          <label htmlFor="" className="text-gray-700 text-sm font-bold mb-2">
            Content
          </label>
          <textarea
            onChange={(e) => setContent(e.target.value)}
            className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none"
          />
        </div>
        <button
          type="submit"
          className="py-2 px-4 border rounded-md bg-orange-300"
          disabled={loading}
        >
          submit
        </button>
      </form>
    </div>
  );
};

export default CreateBlogPage;
