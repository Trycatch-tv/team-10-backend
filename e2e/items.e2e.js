const request = require("supertest");

const createApp = require("../app");

describe("tests for users path", () => {
  let app = null;
  let server = null;
  let api = null;

  beforeEach(() => {
    app = createApp();
    server = app.listen(2000);
    api = request(app);
  });

  describe("GET /items", () => {
    test("must return a 404 request not authorized", async () => {
      const { statusCode } = await api
      .get("/api/v1/items/")
      expect(statusCode).toBe(401);
    });
  });

  afterEach(() => {
    server.close();
  });
});
