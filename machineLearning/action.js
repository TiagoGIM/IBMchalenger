/**
 *
 * main() será executado quando você chamar essa ação
 *
 * @param As ações do Cloud Functions aceitam um único parâmetro, que deve ser um objeto JSON.
 *
 * @return A saída dessa ação, que deve ser um objeto JSON.
 *
 */
var btoa = require("btoa");
var request = require("request");

function main(params) {
  // Coloque sua apikey da machine learning
  var apikey = "SuaAPI";

  // Use this code as written to get an access token from IBM Cloud REST API
  var IBM_Cloud_IAM_uid = "bx";
  var IBM_Cloud_IAM_pwd = "bx";

  const getToken = async () => {
    var options = {
      url: "https://iam.bluemix.net/oidc/token",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        Authorization:
          "Basic " + btoa(IBM_Cloud_IAM_uid + ":" + IBM_Cloud_IAM_pwd),
      },
      body:
        "apikey=" +
        apikey +
        "&grant_type=urn:ibm:params:oauth:grant-type:apikey",
      json: true,
    };
    return new Promise((resolve, reject) => {
      request.post(options, function (error, response, body) {
        if (error) reject(error);
        resolve(body.access_token);
      });
    });
  };

  return new Promise((resolve, reject) => {
    const body = {
      fields: ["viagem", "bebida", "genero", "hobby"],
      values: [[params.viagem, params.bebida, params.genero, params.hobby]],
    };

    getToken()
      .then((token) => {
        const options = {
          // TODO: Substituir com SCORING END-POINT do Deployment do Modeler flow
          url: "SuaURL",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
          body,
          json: true,
        };
        request.post(options, (error, resp, data) => {
          if (error) reject(error);
          else if (data.errors) {
            resolve({
              err: true,
              produto: data.errors[0].message,
            });
          } else {
            resolve({
              err: false,
              produto: data.values[0][0],
            });
          }
        });
      })
      .catch((err) => reject(err));
  });
}
