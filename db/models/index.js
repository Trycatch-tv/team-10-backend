const { Stores, StoresSchema } = require('./stores.model');
const { Items, ItemsSchema } = require('./items.model');
const { Users, UserSchema } = require('./users.model');

function setupModels(sequelize) {
    Stores.init(StoresSchema, Stores.config(sequelize));
    Items.init(ItemsSchema, Items.config(sequelize));
    Users.init(UserSchema, Users.config(sequelize));

    Stores.associate(sequelize.models);
    Items.associate(sequelize.models);
}
  
  module.exports = setupModels;