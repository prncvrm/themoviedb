(function () {
  'use strict';

  angular
    .module('movie_db.authentication', [
      'movie_db.authentication.controllers',
      'movie_db.authentication.services'
    ]);

  angular
    .module('movie_db.authentication.controllers', []);

  angular
    .module('movie_db.authentication.services', ['ngCookies']);
})();