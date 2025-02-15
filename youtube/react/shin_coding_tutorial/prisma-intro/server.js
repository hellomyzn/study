const { PrismaClient } = require("@prisma/client");
const express = require("express");
const req = require("express/lib/request");
const app = express();
const PORT = 3000;

const prisma = new PrismaClient();

app.use(express.json());

app.get("/", async (req, res) => {
  const posts = await prisma.posts.findMany();
  return res.json(posts);
});

app.get("/:id", async (req, res) => {
  const id = req.params.id;
  const post = await prisma.posts.findUnique({ where: { id: Number(id) } });
  return res.json(post);
});

app.post("/", async (req, res) => {
  const { title, body } = req.body;
  const posts = await prisma.posts.create({
    data: {
      title: title,
      body: body,
    },
  });
  res.json(posts);
});

app.put("/:id", async (req, res) => {
  const id = req.params.id;
  const { title, body } = req.body;
  const updatedPost = await prisma.posts.update({
    where: {
      id: Number(id),
    },
    data: {
      title: title,
      body: body,
    },
  });
  res.json(updatedPost);
});

app.delete("/:id", async (req, res) => {
  const id = req.params.id;
  const post = await prisma.posts.delete({ where: { id: Number(id) } });
  return res.json(post);
});

app.listen(PORT, () => {
  console.log("start server...");
});
