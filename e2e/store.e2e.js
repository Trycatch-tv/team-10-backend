const request = require("supertest");

const createApp = require("../app");
const { models } = require("./../libs/sequelize");

describe("tests for users path", () => {
  let app = null;
  let server = null;
  let api = null;

  beforeEach(() => {
    app = createApp();
    server = app.listen(2000);
    api = request(app);
  });

  describe("GET /stores", () => {
    test("", async () => {
      const { statusCode } = await api.get("/api/v1/stores/");
      expect(statusCode).toBe(200);
    });
    test("should return a stores", async () => {
      const user = await models.Stores.findByPk("1");
      const { statusCode, body } = await api.get(`/api/v1/stores/1`);
      expect(statusCode).toEqual(200);
      expect(body.id).toEqual(user.id);
    });
  });

  describe("PUT /stores", () => {
    test("return edit a stores valid", async () => {
      const store = await models.Stores.findByPk("4");
      const inputData = {
        name: "tienda2",
      };
      const { statusCode } = await api
        .patch(`/api/v1/stores/${store.id}`)
        .send(inputData);
      expect(statusCode).toEqual(201);
    });
  });

  afterEach(() => {
    server.close();
  });
});
