var app = angular.module('unihdgeo', []).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});

app.factory('lobby', function() {
    var players = [];
    var LobbyService = {};
    
    LobbyService.addPlayer = function(player) {
    	players.push(player);
    };
    LobbyService.removePlayer = function(player) {
        var index = players.indexOf(player);
        players.splice(index, 1);
    };
    LobbyService.players = function() {
        return players;
    };
    
    return LobbyService;
});