const Joi = require("joi");

const id = Joi.number();
const name = Joi.string();
const price = Joi.number();
const store_id = Joi.number();

const createItemSchema = Joi.object({
  name: name.required(),
  price: price.required(),
  store_id: store_id.required(),
});

const updateItemSchema = Joi.object({
  name: name,
  price: price,
  store_id: store_id,
});

const getItemsSchema = Joi.object({
  id: id.required(),
});

const deleteItemsSchema = Joi.object({
  name: name.required(),
});

module.exports = {
  createItemSchema,
  updateItemSchema,
  getItemsSchema,
  deleteItemsSchema
};
