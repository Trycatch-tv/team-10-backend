const boom = require('@hapi/boom');

const { models }= require('./../libs/sequelize');

class ItemsService {

  async create(data) {
    try {
      const newItem = await models.Items.create(data);
      return newItem;
    } catch (error) {
      throw boom.badRequest('Error creating item', error);
    }
  }

  async find() {
      const items = await models.Items.findAll();
      return items;
  }

  async findOne(name) {
    const item = await models.Items.findOne({
      where: { name }
    });
  
    if (!item) {
      throw boom.notFound("Item not found");
    }
  
    return item;
  }

  async findOneStore(id) {
    const items = await models.Items.findAll({
      where: {
        store_id: id
      }
    });
      if (!items) {
        throw boom.notFound('Item not found');
      }
      return items;
  }

  async update(name, changes) {
    try {
      const model = await this.findOne(name);
      const rta = await model.update(changes);
      return rta;
    } catch (error) {
      throw boom.badRequest('Error updating item', error);
    }
  }

  async delete(name) {
    try {
      const model = await this.findOne(name);
      await model.destroy();
      return { rta: true };
    } catch (error) {
      throw boom.badRequest('Error deleting item', error);
    }
  }

}

module.exports = ItemsService;
