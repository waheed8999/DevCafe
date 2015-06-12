/**
* MarketplaceController
* @namespace devcafe.marketplace.controllers
*/
(function () {
  'use strict';

  angular
    .module('devcafe.marketplace.controllers')
    .controller('MarketplaceDetailController', MarketplaceDetailController);

  MarketplaceDetailController.$inject = ['$http', '$location','$scope', '$routeParams', 'Market'];

  function MarketplaceDetailController($http, $location, $scope, $routeParams, Market) {
    var vm = this;
    vm.AddComment = AddComment;
    // var appId = null;
    // vm.Like = Like;
    Market.get($routeParams.id).success(function(data, status, headers, config) {
      // console.log(data);
      $scope.appId = data;
      $scope.appIdRating = data.avg_rating;
      console.log($scope.appId.avg_rating);
    })

    $scope.rateFunction = function(id, value) {
      Market.rate(id, value);
    };

    function AddComment(item, text) {
      var id = item;
      // console.log(item);
      // console.log(text);
      Market.comment(id, text);
    }



  }
})();