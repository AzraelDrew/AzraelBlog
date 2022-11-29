"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _vue = _interopRequireDefault(require("vue"));

var _vuex = _interopRequireDefault(require("vuex"));

var _axios = _interopRequireDefault(require("axios"));

var _qs = _interopRequireDefault(require("qs"));

var _router = _interopRequireDefault(require("../router"));

var _elementUi = require("element-ui");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

_vue["default"].use(_vuex["default"]);

var _default = new _vuex["default"].Store({
  state: {
    currentname: '',
    loginmessage: '',
    userinfo: {},
    baseurl: 'http://127.0.0.1:8000/'
  },
  getters: {
    // 查询登录状态
    loginState: function loginState(state) {
      return state.userinfo.token;
    }
  },
  // mutations用于更改state 且只能在mutations中更改
  mutations: {
    svaeUserInfo: function svaeUserInfo(state, userinfo) {
      state.userinfo = userinfo;
    },
    // 清楚用户登录状态
    clearUserInfo: function clearUserInfo(state) {
      state.userinfo = {};
    }
  },
  actions: {
    // 登录
    // 第一个参数为调用mutations中的方法的函数  第二个参数为 Vue component中的数据
    blogLogin: function blogLogin(_ref, fromData) {
      var _this = this;

      var commit = _ref.commit;
      (0, _axios["default"])({
        url: this.state.baseurl + 'api/azrael-login/',
        method: 'POST',
        data: _qs["default"].stringify(fromData)
      }).then(function (res) {
        if (res.data === 'none') {
          (0, _elementUi.Notification)({
            title: '错误',
            message: '用户不存在！',
            type: 'error'
          });
          return;
        }

        if (res.data === 'pwderr') {
          (0, _elementUi.Notification)({
            title: '错误',
            message: '密码错误！',
            type: 'error'
          });
          return;
        } // Notification({
        //   title: '成功',
        //   message: '登陆成功',
        //   type: 'success',
        // });


        commit('svaeUserInfo', res.data); // 缓存token到本地实现自动登录

        localStorage.setItem('token', res.data.token);
        _this.state.currentname = res.data.nickname;

        _router["default"].push({
          name: 'Home'
        });
      });
    },
    // 注册
    blogRegister: function blogRegister(_ref2, fromData) {
      var _this2 = this;

      var commit = _ref2.commit;
      (0, _axios["default"])({
        url: this.state.baseurl + 'api/azrael-register/',
        method: 'POST',
        data: _qs["default"].stringify(fromData)
      }).then(function (res) {
        if (res.data === 'repeat') {
          (0, _elementUi.Notification)({
            title: '警告',
            message: '用户已注册！',
            type: 'warning'
          });
          return;
        }

        commit('svaeUserInfo', res.data); // 缓存token到本地实现自动登录

        localStorage.setItem('token', res.data.token);
        _this2.state.currentname = res.data.nickname;

        _router["default"].push({
          name: 'Home'
        });

        console.log(res.data);
      });
      window.location.href = window.location.href;
    },
    // 自动登录
    autoLogin: function autoLogin(_ref3) {
      var _this3 = this;

      var commit = _ref3.commit;
      var token = localStorage.getItem('token');
      this.state.currentname = localStorage.getItem('username');

      if (token) {
        (0, _axios["default"])({
          url: this.state.baseurl + 'api/auto-login/',
          method: 'POST',
          data: _qs["default"].stringify({
            token: token
          })
        }).then(function (res) {
          if (res.data === 'TokenTimeOut') {
            alert('用户信息过期,请重新登录');
            return;
          }

          commit('svaeUserInfo', res.data); // 缓存token到本地实现自动登录

          localStorage.setItem('token', res.data.token);
          _this3.state.currentname = res.data.nickname;

          _router["default"].push({
            name: 'Home'
          });
        });
      }
    },
    // 登出
    blogLogOut: function blogLogOut(_ref4, token) {
      var commit = _ref4.commit;
      commit('clearUserInfo');
      localStorage.removeItem('token');
      localStorage.removeItem('username');
      (0, _axios["default"])({
        url: this.state.baseurl + 'api/azrael-logout/',
        method: 'POST',
        data: _qs["default"].stringify({
          token: token
        })
      }).then(function (res) {});
    },
    // 用户权限判断
    checkUserPerm: function checkUserPerm(_ref5, checkInfo) {
      var getters, token, contentType, permissions, perm_data;
      return regeneratorRuntime.async(function checkUserPerm$(_context) {
        while (1) {
          switch (_context.prev = _context.next) {
            case 0:
              getters = _ref5.getters;
              // 用户
              token = getters.loginState; // 表

              contentType = checkInfo.contentType; // 权限

              permissions = checkInfo.permissions; // 鉴权结果   必须等axios请求完成返回结果后才执行后面的代码

              _context.next = 6;
              return regeneratorRuntime.awrap((0, _axios["default"])({
                url: this.state.baseurl + 'api/azrael-checkperm/',
                method: 'POST',
                data: _qs["default"].stringify({
                  token: token,
                  contentType: contentType,
                  permissions: JSON.stringify(permissions)
                })
              }).then(function (res) {
                if (res.data === 'nologin') {
                  perm_data = false;
                  alert('用户信息错误');
                  return;
                }

                if (res.data === 'nopermission') {
                  perm_data = false;
                  alert('用户权限不足，请联系管理员');
                  return;
                }

                if (res.data === 'OK') {
                  perm_data = true;
                }
              }));

            case 6:
              return _context.abrupt("return", perm_data);

            case 7:
            case "end":
              return _context.stop();
          }
        }
      }, null, this);
    }
  },
  modules: {}
});

exports["default"] = _default;