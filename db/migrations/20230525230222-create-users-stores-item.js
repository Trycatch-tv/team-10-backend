'use strict';

const { USER_TABLE, UserSchema  } = require('./../models/users.model');
const { STORES_TABLE, StoresSchema  } = require('./../models/stores.model');
const { ITEMS_TABLE, ItemsSchema  } = require('./../models/items.model');

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up (queryInterface) {
    await queryInterface.createTable(STORES_TABLE, StoresSchema);
    await queryInterface.createTable(USER_TABLE, UserSchema);
    await queryInterface.createTable(ITEMS_TABLE, ItemsSchema);
  },

  async down (queryInterface) {
    await queryInterface.dropTable(USER_TABLE);
    await queryInterface.dropTable(STORES_TABLE);
    await queryInterface.dropTable(ITEMS_TABLE);
  }
};
