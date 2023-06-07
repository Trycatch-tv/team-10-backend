const boom = require("@hapi/boom");
const ItemsService = require("./items.service");
const { models } = require("./../libs/sequelize");

const serviceItems = new ItemsService();

class StoreService {
  constructor() {}

  async create(data) {
    try {
      const newStore = await models.Stores.create(data);
      return newStore;
    } catch (error) {
      throw boom.badRequest("Error creating item", error);
    }
  }

  async find() {
    const stores = await models.Stores.findAll();
    const storesWithItems = [];
    for (const store of stores) {
      const items = await serviceItems.findOneStore(store.id);
      storesWithItems.push({ ...store.dataValues, items: items });
    }
    return storesWithItems;
  }

  async findOne(id) {
    const store = await models.Stores.findByPk(id);
    const items = await serviceItems.findOneStore(id);
    if (!store) {
      throw boom.notFound("Store not found");
    }
    return { ...store.dataValues, items: items };
  }

  async update(id, newData) {
    try {
      const [numRowsUpdated, updatedRows] = await models.Stores.update(
        newData,
        {
          where: { id },
          returning: true,
        }
      );

      if (numRowsUpdated === 0) {
        throw boom.notFound("Store not found");
      }

      const updatedStore = updatedRows[0].get();

      return updatedStore;
    } catch (error) {
      throw boom.badRequest("Error updating store", error);
    }
  }

  async delete(name) {
    try {
      const model = await models.Stores.findOne({
        where: { name },
      });

      if (!model) {
        throw boom.notFound("Store not found");
      }

      await model.destroy();
      return { rta: true };
    } catch (error) {
      throw boom.badRequest("Error deleting store", error);
    }
  }
}

module.exports = StoreService;
