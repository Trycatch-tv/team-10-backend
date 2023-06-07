const { Model, DataTypes, Sequelize } = require("sequelize");

const { STORES_TABLE } = require("./stores.model");

const ITEMS_TABLE = "items";

const ItemsSchema = {
  id: {
    allowNull: false,
    autoIncrement: true,
    primaryKey: true,
    type: DataTypes.INTEGER,
  },
  name: {
    type: DataTypes.STRING,
    unique: true,
    allowNull: false,
  },
  price: {
    allowNull: false,
    type: DataTypes.INTEGER,
  },
  createdAt: {
    allowNull: false,
    type: DataTypes.DATE,
    field: "created_at",
    defaultValue: Sequelize.fn("now"),
  },
  store_id: {
    type: DataTypes.INTEGER,
    allowNull: false,
    references: {
      model: STORES_TABLE,
      key: "id",
    },
    onUpdate: "CASCADE",
    onDelete: "CASCADE",
  },
};

class Items extends Model {
  static associate(models) {
    this.belongsTo(models.Stores, {
      as: "store",
      foreignKey: "store_id",
    });
  }

  static config(sequelize) {
    return {
      sequelize,
      tableName: ITEMS_TABLE,
      modelName: "Items",
      timestamps: false,
    };
  }
}

module.exports = { Items, ItemsSchema, ITEMS_TABLE };
