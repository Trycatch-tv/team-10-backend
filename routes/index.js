const express = require("express");

const Items = require('./items.reuter');
const Stores = require('./stores.router');
const Users = require('./users.router');
const Auth = require('./auth.router');

function routerApi(app) {
  const router = express.Router();
  app.use("/api/v1", router);
  router.use('/items', Items)
  router.use('/stores', Stores)
  router.use('/users', Users)
  router.use('/auth', Auth)
}

module.exports = routerApi;
