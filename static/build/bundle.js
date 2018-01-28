/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/*!************************!*\
  !*** ./static/main.js ***!
  \************************/
/*! dynamic exports provided */
/*! all exports used */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
eval("\n\nvar _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if (\"value\" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();\n\nvar _tweet = __webpack_require__(/*! ./components/tweet */ 1);\n\nvar _tweet2 = _interopRequireDefault(_tweet);\n\nfunction _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }\n\nfunction _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError(\"Cannot call a class as a function\"); } }\n\nfunction _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError(\"this hasn't been initialised - super() hasn't been called\"); } return call && (typeof call === \"object\" || typeof call === \"function\") ? call : self; }\n\nfunction _inherits(subClass, superClass) { if (typeof superClass !== \"function\" && superClass !== null) { throw new TypeError(\"Super expression must either be null or a function, not \" + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }\n\nvar Main = function (_React$Component) {\n    _inherits(Main, _React$Component);\n\n    function Main() {\n        _classCallCheck(this, Main);\n\n        return _possibleConstructorReturn(this, (Main.__proto__ || Object.getPrototypeOf(Main)).apply(this, arguments));\n    }\n\n    _createClass(Main, [{\n        key: \"render\",\n        value: function render() {\n            console.log(\"Test render\");\n            return React.createElement(\n                \"div\",\n                null,\n                React.createElement(\n                    \"h1\",\n                    null,\n                    \"Test microservices Architecture\"\n                )\n            );\n        }\n    }]);\n\n    return Main;\n}(React.Component);\n\nvar documentReady = function documentReady() {\n    console.log(\"Test DOM\");\n    ReactDOM.render(React.createElement(Main, null), document.getElementById('react'));\n};\n$(documentReady);//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiMC5qcyIsInNvdXJjZXMiOlsid2VicGFjazovLy9zdGF0aWMvbWFpbi5qcz80NWExIl0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCBUd2VldCBmcm9tIFwiLi9jb21wb25lbnRzL3R3ZWV0XCI7XG5jbGFzcyBNYWluIGV4dGVuZHMgUmVhY3QuQ29tcG9uZW50IHtcbiAgICByZW5kZXIoKSB7XG4gICAgICAgIGNvbnNvbGUubG9nKFwiVGVzdCByZW5kZXJcIilcbiAgICAgICAgcmV0dXJuIChcbiAgICAgICAgICAgIDxkaXY+XG4gICAgICAgICAgICAgICAgPGgxPlRlc3QgbWljcm9zZXJ2aWNlcyBBcmNoaXRlY3R1cmU8L2gxPlxuICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICk7XG4gICAgfVxufVxubGV0IGRvY3VtZW50UmVhZHkgPSAoKSA9PiB7XG4gICAgY29uc29sZS5sb2coXCJUZXN0IERPTVwiKVxuICAgIFJlYWN0RE9NLnJlbmRlcihcbiAgICAgICAgPE1haW4gLz4sXG4gICAgICAgIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdyZWFjdCcpXG4gICAgKTtcbn07XG4kKGRvY3VtZW50UmVhZHkpO1xuXG5cbi8vIFdFQlBBQ0sgRk9PVEVSIC8vXG4vLyBzdGF0aWMvbWFpbi5qcyJdLCJtYXBwaW5ncyI6Ijs7OztBQUFBO0FBQ0E7Ozs7Ozs7Ozs7O0FBQUE7Ozs7Ozs7Ozs7O0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFBQTtBQUNBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFEQTtBQUlBOzs7O0FBUkE7QUFDQTtBQVNBO0FBQ0E7QUFDQTtBQUlBO0FBQ0EiLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///0\n");

/***/ }),
/* 1 */
/*!************************************!*\
  !*** ./static/components/tweet.js ***!
  \************************************/
/*! dynamic exports provided */
/*! all exports used */
/***/ (function(module, exports, __webpack_require__) {

"use strict";
eval("\n\nfunction Tweet(data) {\n  this.id = ko.observable(data.id);\n  this.username = ko.observable(data.tweetedby);\n  this.body = ko.observable(data.body);\n  this.timestamp = ko.observable(data.timestamp);\n}\n\nfunction TweetListViewModel() {\n  var self = this;\n  self.tweets_list = ko.observableArray([]);\n  self.username = ko.observable();\n  self.body = ko.observable();\n  self.addTweet = function () {\n    self.save();\n    self.username(\"\");\n    self.body(\"\");\n  };\n\n  $.getJSON('/api/v1/tweets', function (tweetModels) {\n    var t = $.map(tweetModels.tweets_list, function (item) {\n      return new Tweet(item);\n    });\n    self.tweets_list(t);\n  });\n\n  self.save = function () {\n    return $.ajax({\n      url: '/api/v1/tweets',\n      contentType: 'application/json',\n      type: 'POST',\n      data: JSON.stringify({\n        'username': self.username(),\n        'body': self.body()\n      }),\n      success: function success(data) {\n        alert(\"success\");\n        console.log(\"Pushing to users array\");\n        self.push(new Tweet({\n          username: data.username, body: data.body\n        }));\n        return;\n      },\n\n      error: function error() {\n        return console.log(\"Failed\");\n      }\n\n    });\n  };\n}\n\nko.applyBindings(new TweetListViewModel());//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiMS5qcyIsInNvdXJjZXMiOlsid2VicGFjazovLy9zdGF0aWMvY29tcG9uZW50cy90d2VldC5qcz9iMTliIl0sInNvdXJjZXNDb250ZW50IjpbImZ1bmN0aW9uIFR3ZWV0KGRhdGEpIHtcbiAgdGhpcy5pZCA9IGtvLm9ic2VydmFibGUoZGF0YS5pZCk7XG4gIHRoaXMudXNlcm5hbWUgPSBrby5vYnNlcnZhYmxlKGRhdGEudHdlZXRlZGJ5KTtcbiAgdGhpcy5ib2R5ID0ga28ub2JzZXJ2YWJsZShkYXRhLmJvZHkpO1xuICB0aGlzLnRpbWVzdGFtcCA9IGtvLm9ic2VydmFibGUoZGF0YS50aW1lc3RhbXApO1xufVxuXG5mdW5jdGlvbiBUd2VldExpc3RWaWV3TW9kZWwoKSB7XG4gIHZhciBzZWxmID0gdGhpcztcbiAgc2VsZi50d2VldHNfbGlzdCA9IGtvLm9ic2VydmFibGVBcnJheShbXSk7XG4gIHNlbGYudXNlcm5hbWUgPSBrby5vYnNlcnZhYmxlKCk7XG4gIHNlbGYuYm9keSA9IGtvLm9ic2VydmFibGUoKTtcbiAgc2VsZi5hZGRUd2VldCA9IGZ1bmN0aW9uICgpIHtcbiAgICBzZWxmLnNhdmUoKTtcbiAgICBzZWxmLnVzZXJuYW1lKFwiXCIpO1xuICAgIHNlbGYuYm9keShcIlwiKTtcbiAgfTtcblxuICAkLmdldEpTT04oJy9hcGkvdjEvdHdlZXRzJywgZnVuY3Rpb24gKHR3ZWV0TW9kZWxzKSB7XG4gICAgdmFyIHQgPSAkLm1hcCh0d2VldE1vZGVscy50d2VldHNfbGlzdCwgZnVuY3Rpb24gKGl0ZW0pIHtcbiAgICAgIHJldHVybiBuZXcgVHdlZXQoaXRlbSk7XG4gICAgfSk7XG4gICAgc2VsZi50d2VldHNfbGlzdCh0KTtcbiAgfSk7XG5cbiAgc2VsZi5zYXZlID0gZnVuY3Rpb24gKCkge1xuICAgIHJldHVybiAkLmFqYXgoe1xuICAgICAgdXJsOiAnL2FwaS92MS90d2VldHMnLFxuICAgICAgY29udGVudFR5cGU6ICdhcHBsaWNhdGlvbi9qc29uJyxcbiAgICAgIHR5cGU6ICdQT1NUJyxcbiAgICAgIGRhdGE6IEpTT04uc3RyaW5naWZ5KHtcbiAgICAgICAgJ3VzZXJuYW1lJzogc2VsZi51c2VybmFtZSgpLFxuICAgICAgICAnYm9keSc6IHNlbGYuYm9keSgpLFxuICAgICAgfSksXG4gICAgICBzdWNjZXNzOiBmdW5jdGlvbiAoZGF0YSkge1xuICAgICAgICBhbGVydChcInN1Y2Nlc3NcIilcbiAgICAgICAgY29uc29sZS5sb2coXCJQdXNoaW5nIHRvIHVzZXJzIGFycmF5XCIpO1xuICAgICAgICBzZWxmLnB1c2gobmV3IFR3ZWV0KHtcbiAgICAgICAgICB1c2VybmFtZTogZGF0YS51c2VybmFtZSwgYm9keTpcbiAgICAgICAgICAgIGRhdGEuYm9keVxuICAgICAgICB9KSk7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH0sXG5cbiAgICAgIGVycm9yOiBmdW5jdGlvbiAoKSB7XG4gICAgICAgIHJldHVybiBjb25zb2xlLmxvZyhcIkZhaWxlZFwiKTtcbiAgICAgIH1cbiAgICAgIFxuICAgIH0pO1xuICB9O1xufVxuXG5rby5hcHBseUJpbmRpbmdzKG5ldyBUd2VldExpc3RWaWV3TW9kZWwoKSk7XG5cblxuLy8gV0VCUEFDSyBGT09URVIgLy9cbi8vIHN0YXRpYy9jb21wb25lbnRzL3R3ZWV0LmpzIl0sIm1hcHBpbmdzIjoiOztBQUFBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUZBO0FBSUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQURBO0FBSUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFyQkE7QUF1QkE7QUFDQTtBQUNBO0FBQ0EiLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///1\n");

/***/ })
/******/ ]);