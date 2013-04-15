function LobbyCtrl($scope, $http, lobby, $location) {
	console.log("Path: "+$location.path());
	$http.get('/lobby/'+$scope.lobby_id+'/list').success(function(data){
		console.log(data);
		
		//$scope.players = lobby;
	});
}