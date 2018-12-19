# coding=utf-8
from lxml import etree


def getList(a):
    # print a
    if a:
        if a[0].isdigit():
            return a[0]
        return a[0].strip().endcode('utf8')
    else:
        return ""


def getListStr(a):
    print a
    if a:
        return a[0][0].xpath('string(.)').etract()
    else:
        return ""


wb_data = """

<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta http-equiv="Cache-Control" content="no-transform" /><meta http-equiv="Cache-Control" content="no-siteapp" /><meta http-equiv="Content-language" content="zh-CN" /><meta name="format-detection" content="telephone=no" /><meta name="applicable-device" content="pc"><link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.lianjia.com/sh/zufang/" >
<meta name="mobile-agent" content="format=html5;url=https://m.lianjia.com/sh/zufang/"><script>
ljConf = {
    city_id: '310000',
    city_abbr: 'sh',
    city_name: '上海',
    channel: 'zufang',
    page: 'zufang_search',
    pageConfig: {"ajaxroot":"\/\/ajax.api.lianjia.com\/","imAppid":"LIANJIA_WEB_20160624","imAppkey":"6dfdcee27d78b1107fceeca55d80b7bd"},
    feroot: '//s1.ljcdn.com/feroot/',
    ucid:'',
    cdn:'0',
};
</script>

<!-- 2017.11.8 市场需求加上新的统计 -->
<!-- 2017.7.18 开放全国 -->
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?9152f8221cb6243a53c83b956842be8a";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
<script src="https://s1.ljcdn.com/feroot/pc/asset/common/tingyun-rum.js?_v=20181206222953"></script><title>上海租房_上海租房网_上海房屋出租(上海链家网)</title>
<meta name="description" content="链家上海租房网,现有真实房屋租赁25787套.为需要房屋租出租赁的用户提供区域租房和地铁租房,方便您更快捷的了解找到合适的居住房屋.在上海租房就到上海链家网. " />
<meta name="keywords" content="上海租房网,上海租房,上海个人房源出租,上海房屋出租,上海房屋租赁 " />
<link href="/favicon.ico" type="image/x-icon" rel=icon><link href="/favicon.ico" type="image/x-icon" rel="shortcut icon"><link rel="stylesheet" href="https://s1.ljcdn.com/feroot/pc/asset/common.css?_v=20181206222953">
<link rel="stylesheet" href="https://s1.ljcdn.com/feroot/pc/asset/list.css?_v=20181206222953">
<!--[if lt IE 9]><script type="text/javascript" src="https://s1.ljcdn.com/feroot/dep/common-require/html5.js?_v=20181206222953"></script><![endif]-->
<script>
function RESIZEIMG(b,k,l,m){var c=b.parentNode;var d=parseInt(c.offsetWidth)||k;var e=parseInt(c.offsetHeight)||l;var f=d/e;var g=b.naturalWidth||b.width;var h=b.naturalHeight||b.height;var i=g/h;var j="width";if(f<i){j="height";try{b.style["left"]="-"+parseInt(Math.abs((d-(g*e/h))/2))+"px"}catch(e){}}else if(m){try{b.style["top"]="-"+parseInt(Math.abs((e-(h*d/g))/2))+"px"}catch(e){}};b.style[j]="100%";};
</script>
<script>
var _czc = _czc || [];
_czc.push(["_setAccount", "1254525948"]);
</script>

<script type="text/javascript">
var _smq = _smq || [];
_smq.push(['_setAccount', '41331c2', new Date()]);
_smq.push(['_setDomainName', 'lianjia.com']);
_smq.push(['pageview']);
(function() {
var sm = document.createElement('script'); sm.type = 'text/javascript'; sm.async = true;
sm.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'cdnmaster.com/sitemaster/collect.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(sm, s);
})();
</script>
</head><body><script>
__STAT_LJ_CONF = {
    params: {
        ljweb_group: ['SEARCH','BIGDATA_PC'],
        ljweb_id: '',
        ljweb_mod: '',
        ljweb_bl: '',
        ljweb_el: '',
        ljweb_sl: '',
        ljweb_index: '',
        ljweb_value: '',
        ljweb_url: '',
        ljweb_ljref: (document.cookie.match(/(?:^| )ljref=([^;]*)(?:;|$)/) || ['',''])[1],
        ljweb_sample: (document.cookie.match(/(?:^| )sample_traffic_test=([^;]*)(?:;|$)/) || ['',''])[1],
        ljweb_ref: document.referrer,
        ljweb_cid: '310000',
        ljweb_channel: 'zufang',
        ljweb_page: 'zufang_search',
        ljweb_source: '',
        ljweb_stat_id: ''
    }
};



var UT = {
    send: function() {

    }
};
var LjUserTrack = {
    log: [],
    initInterval: false,
    intervalLog: function() {
        setTimeout(function() {
            if(window.$ULOG && $ULOG.send) {
                for(var i = 0, l = LjUserTrack.log.length; i < l; i++) {
                    LjUserTrack.__send(LjUserTrack.log[i]);
                }

                for(var m = 0, n = LjUserTrack.logIds.length; m < n; m++) {
                    LjUserTrack.__sendId(LjUserTrack.logIds[m]);
                }
                for(var j = 0, k = LjUserTrack.logDatas.length; j < k; j++) {
                    LjUserTrack.__sendData(LjUserTrack.logDatas[j].id, LjUserTrack.logDatas[j].data);
                }
            } else {
                LjUserTrack.intervalLog();
            }
        }, 16.7);
    },
    _start_time: +new Date,
    logDatas: [],
    __sendData: function(id, data) {
        if(id && (typeof(data) == 'object')){
          data.pid = (window.__UDL_CONFIG && window.__UDL_CONFIG.pid && window.__UDL_CONFIG.pid)||"lianjiaweb";
          data.key = window.location.href;
          window.$ULOG && $ULOG.send(id, data);
        }
    },
    sendData: function(id, data) {
        if(window.$ULOG && $ULOG.send) {
            LjUserTrack.__sendData(id, data);
        } else {
            LjUserTrack.logDatas.push({id: id, data: data});

            LjUserTrack.initInterval || (LjUserTrack.initInterval = true, LjUserTrack.intervalLog());

        }
    },
    __send: function(data) {
        var evt_id = data.evt_id || '10043';
        if('evt_id' in data) {
            delete data.evt_id;
        }

        window.$ULOG && $ULOG.send(evt_id, {
            "pid": (window.__UDL_CONFIG && window.__UDL_CONFIG.pid && window.__UDL_CONFIG.pid)||"lianjiaweb",
            "key": window.location.href,
            "action": data
        });
    },
    logIds: [],
    __sendId: function(id) {
        id && window.$ULOG && window.$ULOG && $ULOG.send(id, {
            "pid": (window.__UDL_CONFIG && window.__UDL_CONFIG.pid && window.__UDL_CONFIG.pid)||"lianjiaweb",
            "key": window.location.href
        });
    },
    sendId: function(id) {
        if(window.$ULOG && $ULOG.send) {
            LjUserTrack.__sendId(id);
        } else {
            LjUserTrack.logIds.push(id);

            LjUserTrack.initInterval || (LjUserTrack.initInterval = true, LjUserTrack.intervalLog());

        }
    },
    send: function(data, el, config) {

        var utConf = __STAT_LJ_CONF;
        var params = config || utConf.params,
            win = window,
            j;

        data.groupIndex = data.ljweb_group || 0;

        if (params) {
            for (var d in params) {
                if(params[d] !== j && data[d] === j) {
                    data[d] = params[d];
                }
            }
        }

        if(el) {
            this.checkClick(el, data);
        }

        data.ljweb_group = params['ljweb_group'][data.groupIndex || 0];

        delete data.groupIndex;

        if(data.typ) {
            data.ljweb_bl = (data.ljweb_bl || '') + '_' + data.typ;
            delete data.typ;
        }

        if(window.$ULOG && $ULOG.send) {
            LjUserTrack.__send(data);
        } else {
            LjUserTrack.log.push(data);

            LjUserTrack.initInterval || (LjUserTrack.initInterval = true, LjUserTrack.intervalLog());

        }

    },
    checkClick: function(el, data) {

        var TAG_LINK = 'A';
        var href = '';
        var elParent = null;

        href = (el.tagName.toUpperCase() === TAG_LINK ? el.getAttribute("href", 2) : '');
        if(!href && (elParent = el.parentNode) && elParent.nodeType === 1) {
            href = (elParent.tagName.toUpperCase() === TAG_LINK ? elParent.getAttribute("href", 2) : '');
        }

        if(href) {
            data.ljweb_url = href;
        } else {
            data.ljweb_url = data.ljweb_url
                  || el.getAttribute("data-log_url")
                  || (elParent=el.parentNode||el).getAttribute("data-log_url")
                  || (
                        (elParent=elParent.parentNode||elParent)
                     && (elParent.nodeType === 1)
                     && elParent.getAttribute("data-log_url")
                     )
                  || "";
        }

        this.attr(el, data);

    },
    path: function() {

    },
    attr: function(el, data) {
        var modId     = el.getAttribute("log-mod");
        var blAttr    = el.getAttribute("data-bl");
        var elAttr    = el.getAttribute("data-el");
        var slAttr    = el.getAttribute("data-sl");
        var InAttr    = el.getAttribute("data-log_index");
        var valAttr   = el.getAttribute("data-log_value");
        var idAttr    = el.getAttribute("data-log_id");
        var groupAttr = el.getAttribute("data-log_group");
        var sourceAttr = el.getAttribute("data-log_source");
        var statIdAttr = el.getAttribute("data-log_statId");
        var evtId     = el.getAttribute("data-log_evtid");

        data.ljweb_bl    = data.ljweb_bl || blAttr || '';
        data.ljweb_el    = data.ljweb_el || elAttr || '';
        data.ljweb_sl    = data.ljweb_sl || slAttr || '';
        data.ljweb_index = data.ljweb_index || InAttr || '';
        data.ljweb_value = data.ljweb_value || valAttr || '';
        data.ljweb_id    = data.ljweb_id || idAttr || '';
        data.ljweb_source    = data.ljweb_source || sourceAttr || '';
        data.ljweb_stat_id    = data.ljweb_stat_id || statIdAttr || 0;
        data.groupIndex  = data.groupIndex || groupAttr || 0;
        data.evt_id      = data.evt_id || evtId || '';

        if (!modId) {
            if (el.parentNode && el.parentNode.nodeType === 1 && el.parentNode.tagName.toUpperCase() !== 'BODY') {
                this.attr(el.parentNode, data);
            }
        } else {
            data.ljweb_mod = modId;
        }
    }
};

;;(function() {
    var isW3c = !!document.addEventListener;

    LjUserTrack.send({
        ljweb_mod: 'pv',
        ljweb_group: 1
    });

    /*window[isW3c ? 'addEventListener' : 'attachEvent'](
        (isW3c ? '': 'on') + 'beforeunload',
        function(e) {
            var _end_time = +new Date;
            UT.send({type: 'show', subtype: 'stay', time: (_end_time-UT._start_time)/1000});
        },
        false);*/
})();





</script>


<header class="lianjia-header "><div class="nav-wrap"><div class="wrapper "><div class="fl"><a class="logo" href="//www.lianjia.com/"  title="链家房产网"><!-- <img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/logo.png?_v=20181206222953"> --></a></div><div class="fr nav  "><div class="fl"><ul>
		                          <li>
                <a  class="" href="https://sh.lianjia.com/ershoufang/" >二手房</a>
            </li>
          	    		                          <li>
                <a  class="" href="https://sh.fang.lianjia.com/" >新房</a>
            </li>
          	    		                          <li>
                <a  class="on" href="https://sh.lianjia.com/zufang/" >租房</a>
            </li>
          	    		                          <li>
                <a  class="" href="https://us.lianjia.com" >海外</a>
            </li>
          	    		                          <li>
                <a  class="" href="https://shang.lianjia.com/sh" >商业办公</a>
            </li>
          	    		                          <li>
                <a  class="" href="https://sh.lianjia.com/xiaoqu/" >小区</a>
            </li>
          	    		                          <li>
                <a  class="" href="https://sh.lianjia.com/jingjiren/" >经纪人</a>
            </li>
          	    		    	        <li class="hover">
	            <a  class="" href="https://sh.lianjia.com/wenda/" >
	            指南
	            </a>
	            <div class="nav-list">
	                <dd>
	                    <i></i>
	                                                                                <dl>
                                    <a href="https://sh.lianjia.com/wenda/" >问答</a>
                                </dl>
                                                                                                                <dl>
                                    <a href="https://news.lianjia.com/sh/baike/" >百科</a>
                                </dl>
                                                    	                </dd>
	            </div>
	        </li>
	    		                          <li>
                <a  class="" href="https://sh.lianjia.com/tool.html" target="_blank">工具</a>
            </li>
          	    		                          <li>
                <a  class="" href="https://sh.lianjia.com/yezhu/" target="_blank">发布房源</a>
            </li>
          	    	</ul></div><div class="fr login"><div class="ti-hover"><div class="login-panel typeUserInfo"><script type="text/template" class="template">
      <%if(data && data.username){%>
        <%if(data.isAgent){%>
         <a href="<%=$.env.fixedUrl('//agent.lianjia.com/')%>"><span><%=data.username%></span></a>
        <%}else{%>
          <a href="<%=$.env.fixedUrl('//user.lianjia.com/')%>" rel="nofollow"><span><%=data.username%></span></a>
         <%}%>
         <span id="indexTipContainer"></span>
         <%if(data.isAgent){%>
           <span class="welcome"><a class="reg" href="<%=data.logoutUrl%>" rel="nofollow">退出</a></span>
         <%}else{%>
           <span class="welcome"><a class="reg" href="<%=data.logoutUrl%>" rel="nofollow">退出</a></span>
          <%}%>
      <%}else{%>
        <span class="welcome"><a class="btn-register" href="<%=data.registerUrl%>" rel="nofollow"><span class="log">注册</span></a>|<a class="btn-login bounceIn actLoginBtn" href="<%=data.loginUrl%>"><span class="reg">登录</span></a></span>
      <%}%>
    </script><div class="typeShowUser"><span class="welcome"><a class="btn-register" href="https://passport.lianjia.com/register/resources/lianjia/register.html?service=https%3A%2F%2Fwww.lianjia.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttps%253A%252F%252Fsh.lianjia.com%252Fzufang%252F"  rel="nofollow" ><span class="log">注册</span></a>|<a href="https://upassport.lianjia.com/login?service=https%3A%2F%2Fwww.lianjia.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttps%253A%252F%252Fsh.lianjia.com%252Fzufang%252F" class="btn-login bounceIn actLoginBtn" rel="nofollow"><span class="reg">登录</span></a></span></div></div><div class="user-news" id="userNews"><script type="text/template" id="News">
        <ul>
          <li class="s-li"><span class="userNewsTriangle"></span></li>
        <%for(var i in group_by_type){%>
          <%if(group_by_type[i].unread !== 0 && pushMsgMap.hasOwnProperty(i)){%>
            <li>
              <a href="<%=pushMsgMap[i].url%>">
                <%=$.replaceTpl(pushMsgMap[i].text, {unread:group_by_type[i].unread})%>
              </a>
            </li>
          <%}%>
        <%}%>
        </ul>
      </script></div></div>
</div></div></div></div></header>
<!-- NAV头部搜索模块 -->
<div class="searchs"><div class="wrapper"><div class="fl" log-mod="search"><div class="search-txt"><form class="clear" id="searchForm" action="/zufang/rs" data-action="/zufang/rs" method="post"><div class="search-tab"><i class="icon" data-bl="switch"></i><div data-bl="switch" class="check"  formact="/zufang/rs" actdata="zufang">租房</div><ul class="tabs" data-bl="switch"><li><label actData="channel=zufang" formact="/zufang/rs" tra="" tips="请输入区域、板块或小区名开始找房">租房</label></li><li><label formact="/ershoufang/rs" actData="channel=ershoufang" tra="_blank" tips="请输入区域、板块或小区名开始找房">二手房</label></li><li><label formact="/xiaoqu/rs" actData="channel=xiaoqu" tra="_blank" tips="请输入小区名开始查找小区">小区</label></li><li><label formact="/chengjiao/rs" actData="channel=chengjiao" tra="_blank" tips="">成交</label></li><li><label formact="/loupan/rs" actData="channel=xinfang" tra="_blank" tips="请输入楼盘名称开始找房">新房</label></li><li><label formact="/jingjiren/rs" actData="channel=jingjiren" tra="_blank" tips="请输入商圈、小区或经纪人的姓名、电话...">经纪人</label></li></ul><div  class="txt-serach"><input class="left txt" name="keyword" autocomplete="off" placeholder="请输入区域、板块或小区名开始找房" id="keyword-box"><div class="hot-sug" data-bl="sug" data-el="history"><ul id="zufang"><li class="hot-name">热门搜索</li><div class="list"><li><a href="http://sh.lianjia.com/zufang/rs%E9%9D%99%E5%AE%89%E6%96%B0%E5%9F%8E/" data-log_channel="zufang" data-log_index="1" data-log_value="静安新城">静安新城</a></li><li><a href="http://sh.lianjia.com/zufang/rs%E5%A4%A7%E5%8D%8E%E9%94%A6%E7%BB%A3%E5%8D%8E%E5%9F%8E/" data-log_channel="zufang" data-log_index="2" data-log_value="大华锦绣华城">大华锦绣华城</a></li><li><a href="http://sh.lianjia.com/zufang/rs%E4%B8%AD%E8%BF%9C%E4%B8%A4%E6%B9%BE%E5%9F%8E/" data-log_channel="zufang" data-log_index="3" data-log_value="中远两湾城">中远两湾城</a></li><li><a href="http://sh.lianjia.com/zufang/rs%E7%91%9E%E8%99%B9%E6%96%B0%E5%9F%8E/" data-log_channel="zufang" data-log_index="4" data-log_value="瑞虹新城">瑞虹新城</a></li><li><a href="http://sh.lianjia.com/zufang/rs%E9%98%B3%E5%85%89%E5%A8%81%E5%B0%BC%E6%96%AF/" data-log_channel="zufang" data-log_index="5" data-log_value="阳光威尼斯">阳光威尼斯</a></li><li><a href="http://sh.lianjia.com/zufang/rs%E4%B8%8A%E6%B5%B7%E5%BA%B7%E5%9F%8E/" data-log_channel="zufang" data-log_index="6" data-log_value="上海康城">上海康城</a></li></div><li class="del">清除历史记录</li></ul><ul id="ershoufang"><li class="hot-name">热门搜索</li><div class="list"><li><a href="http://sh.lianjia.com/ershoufang/rs%E4%B8%8A%E6%B5%B7%E5%BA%B7%E5%9F%8E/" data-log_channel="ershoufang" data-log_index="1" data-log_value="上海康城">上海康城</a></li><li><a href="http://sh.lianjia.com/ershoufang/rs%E6%85%A7%E8%8A%9D%E6%B9%96%E8%8A%B1%E5%9B%AD/" data-log_channel="ershoufang" data-log_index="2" data-log_value="慧芝湖花园">慧芝湖花园</a></li><li><a href="http://sh.lianjia.com/ershoufang/rs%E5%A5%A5%E6%9E%97%E5%8C%B9%E5%85%8B%E8%8A%B1%E5%9B%AD/" data-log_channel="ershoufang" data-log_index="3" data-log_value="奥林匹克花园">奥林匹克花园</a></li><li><a href="http://sh.lianjia.com/ershoufang/rs%E4%B8%AD%E8%BF%9C%E4%B8%A4%E6%B9%BE%E5%9F%8E/" data-log_channel="ershoufang" data-log_index="4" data-log_value="中远两湾城">中远两湾城</a></li><li><a href="http://sh.lianjia.com/ershoufang/rs%E4%B8%9C%E6%96%B9%E6%9B%BC%E5%93%88%E9%A1%BF/" data-log_channel="ershoufang" data-log_index="5" data-log_value="东方曼哈顿">东方曼哈顿</a></li><li><a href="http://sh.lianjia.com/ershoufang/rs%E6%96%B0%E6%B9%96%E6%98%8E%E7%8F%A0%E5%9F%8E/" data-log_channel="ershoufang" data-log_index="6" data-log_value="新湖明珠城">新湖明珠城</a></li><li><a href="http://sh.lianjia.com/ershoufang/rs%E7%BB%8F%E7%BA%AC%E5%9F%8E%E5%B8%82%E7%BB%BF%E6%B4%B2/" data-log_channel="ershoufang" data-log_index="7" data-log_value="经纬城市绿洲">经纬城市绿洲</a></li><li><a href="http://sh.lianjia.com/ershoufang/rs%E4%BF%9D%E5%88%A9%E8%A5%BF%E5%AD%90%E6%B9%BE/" data-log_channel="ershoufang" data-log_index="8" data-log_value="保利西子湾">保利西子湾</a></li></div><li class="del">清除历史记录</li></ul><ul id="xiaoqu"><li class="hot-name">热门搜索</li><div class="list"><li><a href="http://sh.lianjia.com/xiaoqu/rs%E5%A5%A5%E6%9E%97%E5%8C%B9%E5%85%8B%E8%8A%B1%E5%9B%AD/" data-log_channel="xiaoqu" data-log_index="1" data-log_value="奥林匹克花园">奥林匹克花园</a></li><li><a href="http://sh.lianjia.com/xiaoqu/rs%E4%B8%96%E8%8C%82%E6%BB%A8%E6%B1%9F%E8%8A%B1%E5%9B%AD/" data-log_channel="xiaoqu" data-log_index="2" data-log_value="世茂滨江花园">世茂滨江花园</a></li><li><a href="http://sh.lianjia.com/xiaoqu/rs%E4%BF%9D%E5%88%A9%E8%A5%BF%E5%AD%90%E6%B9%BE/" data-log_channel="xiaoqu" data-log_index="3" data-log_value="保利西子湾">保利西子湾</a></li><li><a href="http://sh.lianjia.com/xiaoqu/rs%E6%96%B0%E9%AB%98%E8%8B%91/" data-log_channel="xiaoqu" data-log_index="4" data-log_value="新高苑">新高苑</a></li><li><a href="http://sh.lianjia.com/xiaoqu/rs%E4%B9%9D%E5%9F%8E%E6%B9%96%E6%BB%A8%E5%9B%BD%E9%99%85/" data-log_channel="xiaoqu" data-log_index="5" data-log_value="九城湖滨国际">九城湖滨国际</a></li><li><a href="http://sh.lianjia.com/xiaoqu/rs%E5%90%8C%E6%B6%A6%E8%8F%B2%E8%AF%97%E8%89%BE%E4%BC%A6/" data-log_channel="xiaoqu" data-log_index="6" data-log_value="同润菲诗艾伦">同润菲诗艾伦</a></li><li><a href="http://sh.lianjia.com/xiaoqu/rs%E4%BB%81%E6%81%92%E6%BB%A8%E6%B1%9F%E5%9B%AD/" data-log_channel="xiaoqu" data-log_index="7" data-log_value="仁恒滨江园">仁恒滨江园</a></li></div><li class="del">清除历史记录</li></ul><ul style="border:0;"></ul><ul id="loupan"><li class="hot-name">热门搜索</li><div class="list"><li><a href="http://sh.fang.lianjia.com/loupan/rs%E8%A5%BF%E7%8E%AF%E4%B8%AD%E5%BF%83%E6%98%9F%E4%BF%A1%E5%90%8D%E9%82%B8/" data-log_channel="loupan" data-log_index="1" data-log_value="西环中心星信名邸">西环中心星信名邸</a></li><li><a href="http://sh.fang.lianjia.com/loupan/rs%E8%B7%AF%E5%8A%B2%E4%BD%98%E5%B1%B1%E9%99%A2%E5%AD%90/" data-log_channel="loupan" data-log_index="2" data-log_value="路劲佘山院子">路劲佘山院子</a></li><li><a href="http://sh.fang.lianjia.com/loupan/rs%E4%B8%AD%E9%AA%8F%E5%A4%A9%E6%82%A6/" data-log_channel="loupan" data-log_index="3" data-log_value="中骏天悦">中骏天悦</a></li><li><a href="http://sh.fang.lianjia.com/loupan/rs%E7%A6%B9%E6%B4%B2%E5%BA%9C/" data-log_channel="loupan" data-log_index="4" data-log_value="禹洲府">禹洲府</a></li><li><a href="http://sh.fang.lianjia.com/loupan/rs%E8%87%BB%E6%B0%B4%E5%B2%B8/" data-log_channel="loupan" data-log_index="5" data-log_value="臻水岸">臻水岸</a></li><li><a href="http://sh.fang.lianjia.com/loupan/rs%E5%B0%9A%E6%99%AF%E4%B8%BD%E5%9B%AD/" data-log_channel="loupan" data-log_index="6" data-log_value="尚景丽园">尚景丽园</a></li></div><li class="del">清除历史记录</li></ul><ul style="border:0;"></ul></div><div id="suggest-cont" class="suggest-wrap" data-bl="sug" data-el="sug"></div></div><div class="savesearch" city-id="310000"></div></div><button  type="submit" data-bl="search" data-el="search" class="act-search btn home-ico ico-search LOGCLICKEVTID" target="_blank" daty-id="310000">搜索</button></form></div></div><div class="fr last"><div class="ditu fr"><a href="/dituzufang/" target="_blank"><i></i>地图找房</a></div></div></div></div>


<script  type="text/javascript">
;+function() {

    var oWrap_video_all = document.getElementById('wrap-video-all');
    if(!oWrap_video_all) {
        return;
    }

    oWrap_video_all.onclick = function(){
        var oVideo_box = document.getElementById('video-box');
        var oVideo_close = document.getElementById('video-close');
        oVideo_box.style.display = "block";
        oVideo_close.onclick = function(){
              oVideo_box.style.display = "none";
        }
    }
}();

</script>
<div class="savelist">
    <script type="text/template" id="savesearch">
    <%if(data && data.data){%>
        <span class="s-show"><%=data.count%>条已保存搜索<label></label></span>
        <div class="cunn">
            <ul>
                <li class="title">已保存搜索</li>
                <li class="list">
                    <% for(var i = 0; i < data.data.length;i++){ var dat = data.data;%>
                        <div class="li">
                            <a href="<%=dat[i].url%>" target="_blank">
                                <%if (dat[i].query){%>
                                    <span class="fl se"><%=dat[i].query%></span>
                                <%}%>
                                <span class="fl ti">
                                    <%for(var j = 0; j<dat[i].title.length;j++){%>
                                       <%=dat[i].title[j]%>
                                    <%}%>
                                </span>
                            </a>
                        </div>
                    <%}%>
                </li>
                 <%if (data.data.length > 3) {%>
                    <li class="more">查看全部已保存搜索</li>
                <%}%>
            </ul>
        </div>
    <%}%>
    </script>
</div>



<!-- 面包屑模块 -->
<div class="intro clear" mod-id="lj-common-bread"><div class="container"><div class="fl l-txt"><i class="icon"></i>&nbsp;<a href="/">链家网上海站</a><span class="stp">&nbsp;&gt;&nbsp;</span><span>上海租房</span><h1 class="index_h1">上海租房</h1></div><div class="fr r-txt"></div></div></div><div class="wrapper">
<div class="filter-box"><div class="hd clear"><ul class="tab-lst"><li class="on"><a href="/zufang/"><span>全部租房</span></a></li><li><a href="/ditiezufang/"><span>地铁租房</span></a></li></ul><div class="info"><span class="num">真实房源，假一赔百元，不封顶！</span></div></div><div><div class="bd" id="filter-options"><dl class="dl-lst clear"><dt>区域：</dt><dd data-index="0"><div class="option-list"><a href="/zufang/" class="on">不限</a><a href="/zufang/pudong/">浦东</a><a href="/zufang/minhang/">闵行</a><a href="/zufang/baoshan/">宝山</a><a href="/zufang/xuhui/">徐汇</a><a href="/zufang/putuo/">普陀</a><a href="/zufang/yangpu/">杨浦</a><a href="/zufang/changning/">长宁</a><a href="/zufang/songjiang/">松江</a><a href="/zufang/jiading/">嘉定</a><a href="/zufang/huangpu/">黄浦</a><a href="/zufang/jingan/">静安</a><a href="/zufang/zhabei/">闸北</a><a href="/zufang/hongkou/">虹口</a><a href="/zufang/qingpu/">青浦</a><a href="/zufang/fengxian/">奉贤</a><a href="/zufang/jinshan/">金山</a><a href="/zufang/chongming/">崇明</a><a href="/zufang/shanghaizhoubian/">上海周边</a></div></dd></dl>
<dl class="dl-lst clear"><dt>租金：</dt><dd data-index="1"><div class="option-list"><a href="/zufang/" class="on"rel="nofollow">不限</a><a href="/zufang/rp1/"rel="nofollow">1000元以下</a><a href="/zufang/rp2/"rel="nofollow">1000-2000元</a><a href="/zufang/rp3/"rel="nofollow">2000-4000元</a><a href="/zufang/rp4/"rel="nofollow">4000-6000元</a><a href="/zufang/rp5/"rel="nofollow">6000-8000元</a><a href="/zufang/rp6/"rel="nofollow">8000-12000元</a><a href="/zufang/rp7/"rel="nofollow">12000元以上</a><div class="custom" data-type="price"><div class="txt-box"><input type="text" class="txt" name="min_price" data-index="1" value="" /></div>&nbsp;-&nbsp;<div class="txt-box"><input type="text" class="txt" name="max_price" data-index="1" value="" /></div>&nbsp;元<input type="button" data-type="price" class="ok" value="确定" /></div></div></dd></dl>
<dl class="dl-lst clear"><dt>面积：</dt><dd data-index="2"><div class="option-list"><a href="/zufang/" class="on"rel="nofollow">不限</a><a href="/zufang/ra1/"rel="nofollow">50平以下</a><a href="/zufang/ra2/"rel="nofollow">50-70平</a><a href="/zufang/ra3/"rel="nofollow">70-90平</a><a href="/zufang/ra4/"rel="nofollow">90-110平</a><a href="/zufang/ra5/"rel="nofollow">110-150平</a><a href="/zufang/ra6/"rel="nofollow">150平以上</a><div class="custom" data-type="area"><div class="txt-box"><input type="text" class="txt" name="min_area" data-index="2" value="" /></div>&nbsp;-&nbsp;<div class="txt-box"><input type="text" class="txt" name="max_area" data-index="2" value="" /></div>&nbsp;平<input type="button" data-type="area" class="ok" value="确定" /></div></div></dd></dl>
<dl class="dl-lst clear"><dt>房型：</dt><dd data-index="3"><div class="option-list"><a href="/zufang/" class="on"rel="nofollow">不限</a><a href="/zufang/l1/"rel="nofollow">一室</a><a href="/zufang/l2/"rel="nofollow">二室</a><a href="/zufang/l3/"rel="nofollow">三室</a><a href="/zufang/l4/"rel="nofollow">四室</a><a href="/zufang/l5/"rel="nofollow">五室</a><a href="/zufang/l6/"rel="nofollow">五室以上</a></div></dd></dl>
</div><div class="filter-bar01"><div id="sort-panel" class="sort-panel"><div class="left"><div class="fs14"><span class="left">筛选：</span></div><div class="right"><div class="d-1 dropdown"><span>朝向</span><i></i><ul class="fil-item"><a href="/zufang/f1/"><li>朝东</li></a><a href="/zufang/f2/"><li>朝南</li></a><a href="/zufang/f3/"><li>朝西</li></a><a href="/zufang/f4/"><li>朝北</li></a><a href="/zufang/f5/"><li>南北</li></a></ul></div><div class="d-2 dropdown"><span>楼层</span><i></i><ul class="fil-item"><a href="/zufang/lc1/"><li>低楼层</li></a><a href="/zufang/lc2/"><li>中楼层</li></a><a href="/zufang/lc3/"><li>高楼层</li></a></ul></div><div class="d-3 dropdown"><span>品牌</span><i></i><ul class="fil-item"><a href="/zufang/"><li>全部品牌</li></a><a href="/zufang/bd1/"><li>链家</li></a><a href="/zufang/bd2/"><li>自如</li></a></ul></div><div class="d-4 dropdown"><span>方式</span><i></i><ul class="fil-item"><a href="/zufang/"><li>全部方式</li></a><a href="/zufang/rt1/"><li>整租</li></a><a href="/zufang/rt2/"><li>合租</li></a></ul></div><div class="item-check"><ul><li><a href="/zufang/su1/"><i></i>近地铁</a></li><li><a href="/zufang/rd1/"><i></i>精装修</a></li><li><a href="/zufang/ky1/"><i></i>随时看房</a></li><li><a href="/zufang/idb1/"><i></i>独立阳台</a></li><li><a href="/zufang/pt1/"><i></i>独卫</a></li></ul></div><!-- <div class="item-check"><ul><li><a href="#;" class="check-a"><i></i>满五唯一</a></li><li><a href="#;"><i></i>房本满五年</a></li><li><a href="#;"><i></i>近地铁</a></li><li><a href="#;"><i></i>学区房</a></li><li><a href="#;"><i></i>不限购</a></li></ul></div> --></div></div></div></div><div class="filter-bar01"><div class="sort-bar" id="sort-bar"><span>排序：</span><div class="sort-parent on"><a href="/zufang/"><span>默认</span></a></div><div class="sort-parent"><a href="/zufang/rco10/"><span>最新</span></a></div><div class="sort-parent"><a href="/zufang/rco20/"><span>租金低</span></a></div><div class="sort-parent"><span>面积</span><i></i><ul class="sort-children"><li><a href="/zufang/rco31/">面积从小到大</a></li><li><a href="/zufang/rco32/">面积从大到小</a></li></ul></div></div></div></div></div><div class="main-box clear"><div id="sem_card"></div><div class="con-box"><div class="list-head clear"><h2>共有<span>25787</span>套上海在租房源</h2><div class="view-type" id="viewType"><div class="modeshows modeshow"><span class="l-show view-mod" data-type="real" id="lshow"><i></i>实景图模式</span></div></div></div><div class="list-wrap"><ul id="house-lst" class="house-lst"><li data-index="0" data-log_index="0" data-id="107100796595" data-el="zufang" data-housecode="107100796595" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100796595.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/6d7120d0-2e2e-49d8-9676-a1da0540e855.jpg.280x210.jpg" alt="乾溪新村 2室1厅 4500元" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100796595.html" title="乾溪新村 2室1厅 4500元">乾溪新村 2室1厅 4500元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000016137/" class="laisuzhou"><span class="region">乾溪新村&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">63.24平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/dachangzhen/">大场镇租房</a><span>/</span>高楼层(共6层)<span>/</span>1993年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">4500</span>元/月</div><div class="price-pre">2018.12.01 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="1" data-log_index="1" data-id="107100806357" data-el="zufang" data-housecode="107100806357" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100806357.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/9fa72c0f-1cb9-4d73-9f59-0e8f079bfa40.jpg.280x210.jpg" alt="瑞虹新城六期南北通两房 拎包入住 品质小区" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100806357.html" title="瑞虹新城六期南北通两房 拎包入住 品质小区">瑞虹新城六期南北通两房 拎包入住 品质小区</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011063202151/" class="laisuzhou"><span class="region">瑞虹新城怡庭&nbsp;&nbsp;</span></a><span class="zone"><span>2室2厅&nbsp;&nbsp;</span></span><span class="meters">109.69平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/linpinglu/">临平路租房</a><span>/</span>低楼层(共27层)<span>/</span>2015年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">18000</span>元/月</div><div class="price-pre">2018.11.30 更新</div></div><div class="col-2"><div class="square"><div><span class="num">3</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="2" data-log_index="2" data-id="107100805702" data-el="zufang" data-housecode="107100805702" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100805702.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/86785974-2b46-4581-a8d3-5e63e55e9e47.jpg_600x450.jpg.280x210.jpg" alt="精装修！南北通户型两房！通风采光好！超大双阳台！" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/4a5d072e-7b6d-4ef7-b99b-cd0edcb0a5cd.png.280x210.jpg" /></a></div>


        <div class="info-panel">
            <h2>
                <a target="_blank" href="https://sh.lianjia.com/zufang/107100805702.html" title="精装修！南北通户型两房！通风采光好！超大双阳台！">
                    精装修！南北通户型两房！通风采光好！超大双阳台！
                </a>
            </h2>
            <div class="col-1">
                <div class="where">
                    <a href="https://sh.lianjia.com/xiaoqu/5011000017184/" class="laisuzhou">
                        <span class="region">绿地世纪城(二期)&nbsp;&nbsp;
                        </span>
                    </a> 
                    <span class="zone">
                        <span>
                            2室2厅&nbsp;&nbsp;
                        </span>
                    </span> 
                    <span class="meters">
                        99.41平米&nbsp;&nbsp;
                    </span>
                    <span>
                        南
                    </span>
                </div>
                <div class="other">
                    <div class="con">
                        <a href="https://sh.lianjia.com/zufang/wuning/">武宁租房</a>
                        <span>/</span>
                        高楼层(共33层)
                        <span>/</span>
                        2004年建板楼
                    </div>
                </div>
                <div class="chanquan">
                    <div class="left agency">
                        <div class="view-label left">
                            <span class="fang-subway-ex">
                                <span>近地铁</span>
                            </span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-3">
                <div class="price">
                    <span class="num">9300</span>元/月
                </div>
                <div class="price-pre">
                    2018.12.03 更新
                </div>
            </div>
            <div class="col-2">
                <div class="square">
                    <div>
                        <span class="num">1</span>人
                    </div>
                    <div class="col-look">
                        看过此房
                    </div>
                </div>
            </div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>-->
        </div>
        <div class="pic-panel">
            <a target="_blank" href="https://sh.lianjia.com/zufang/107100773681.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"></a>
        </div>

<div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100773681.html" title="中山北路2451弄 3室2厅 9000元">中山北路2451弄 3室2厅 9000元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000000442/" class="laisuzhou"><span class="region">中山北路2451弄&nbsp;&nbsp;</span></a><span class="zone"><span>3室2厅&nbsp;&nbsp;</span></span><span class="meters">135.4平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/zhenru/">真如租房</a><span>/</span>中楼层(共7层)<span>/</span>1996年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">9000</span>元/月</div><div class="price-pre">2018.12.02 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="4" data-log_index="4" data-id="107100797862" data-el="zufang" data-housecode="107100797862" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100797862.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/5f5fe655-4c67-415b-8e97-d9a8ac8eb221.jpg.280x210.jpg" alt="景城精装修俩房 可长租 价格可谈  详情咨询维护人" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/0e551dba-24ee-49be-885f-7ee02a8c5551.png.280x210.jpg" /></a></div>
<div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100797862.html" title="景城精装修俩房 可长租 价格可谈  详情咨询维护人">景城精装修俩房 可长租 价格可谈  详情咨询维护人</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000003337/" class="laisuzhou"><span class="region">春申景城湖滨晨韵&nbsp;&nbsp;</span></a><span class="zone"><span>2室2厅&nbsp;&nbsp;</span></span><span class="meters">85.3平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/chunshen/">春申租房</a><span>/</span>中楼层(共16层)<span>/</span>2005年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="decoration"></span><span class="decoration-ex"><span>精装修</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">6500</span>元/月</div><div class="price-pre">2018.12.05 更新</div></div><div class="col-2"><div class="square"><div><span class="num">1</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="5" data-log_index="5" data-id="107100801044" data-el="zufang" data-housecode="107100801044" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100801044.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/df3b5cf1-c453-41f3-bb0d-f8cd0fd705f7.jpg.280x210.jpg" alt="大三房 小区靠河位置 楼层好视野棒 人车分流" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/226671d7-9c81-43f1-a64d-89b7d6139cc4.png.280x210.jpg" /></a></div>
<div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100801044.html" title="大三房 小区靠河位置 楼层好视野棒 人车分流">大三房 小区靠河位置 楼层好视野棒 人车分流</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000012368/" class="laisuzhou"><span class="region">未来域&nbsp;&nbsp;</span></a><span class="zone"><span>3室2厅&nbsp;&nbsp;</span></span><span class="meters">122.77平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/sanlin/">三林租房</a><span>/</span>中楼层(共18层)<span>/</span>2006年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">8800</span>元/月</div><div class="price-pre">2018.12.05 更新</div></div><div class="col-2"><div class="square"><div><span class="num">4</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="6" data-log_index="6" data-id="107100706631" data-el="zufang" data-housecode="107100706631" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100706631.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/shfdfs-image/20170513/53893d6b-36c3-4898-9f1a-2e4de697882d.jpg.280x210.jpg" alt="家电齐全，拎包入住，带电梯采光好，不临街，视野开阔" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/6be294ab-6a85-4088-990a-7b4f8fa2187b.png.280x210.jpg" /></a></div>
<div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100706631.html" title="家电齐全，拎包入住，带电梯采光好，不临街，视野开阔">家电齐全，拎包入住，带电梯采光好，不临街，视野开阔</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000010442/" class="laisuzhou"><span class="region">印象欧洲(公寓)&nbsp;&nbsp;</span></a><span class="zone"><span>2室2厅&nbsp;&nbsp;</span></span><span class="meters">79.89平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/huajing/">华泾租房</a><span>/</span>高楼层(共8层)<span>/</span>2011年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="decoration"></span><span class="decoration-ex"><span>精装修</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">6500</span>元/月</div><div class="price-pre">2018.12.06 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="7" data-log_index="7" data-id="107100790669" data-el="zufang" data-housecode="107100790669" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100790669.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/bf8df155-39fd-43dd-95a9-cbb2874b6f82.jpg.280x210.jpg" alt="曹杨九村 2室0厅 5200元" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/f03e95e4-cc52-46d4-a531-ba3667484830.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100790669.html" title="曹杨九村 2室0厅 5200元">曹杨九村 2室0厅 5200元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000013707/" class="laisuzhou"><span class="region">曹杨九村&nbsp;&nbsp;</span></a><span class="zone"><span>2室0厅&nbsp;&nbsp;</span></span><span class="meters">47.8平米&nbsp;&nbsp;</span><span>南 北</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/caoyang/">曹杨租房</a><span>/</span>低楼层(共6层)<span>/</span>1978年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span><span class="haskey"></span><span class="haskey-ex"><span>随时看房</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">5200</span>元/月</div><div class="price-pre">2018.11.29 更新</div></div><div class="col-2"><div class="square"><div><span class="num">10</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="8" data-log_index="8" data-id="107100790077" data-el="zufang" data-housecode="107100790077" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100790077.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/939763f2-5a55-4c9f-86e9-da5b70c0f18a.jpg.280x210.jpg" alt="汇腾南苑 全明两居室 目前已经空关 随时入住" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100790077.html" title="汇腾南苑 全明两居室 目前已经空关 随时入住">汇腾南苑 全明两居室 目前已经空关 随时入住</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000004303/" class="laisuzhou"><span class="region">汇腾南苑&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">77平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/zhoupu/">周浦租房</a><span>/</span>中楼层(共6层)<span>/</span>2007年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"></div></div></div></div><div class="col-3"><div class="price"><span class="num">3000</span>元/月</div><div class="price-pre">2018.11.24 更新</div></div><div class="col-2"><div class="square"><div><span class="num">1</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="9" data-log_index="9" data-id="107100744374" data-el="zufang" data-housecode="107100744374" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100744374.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/ef8ac308-9e31-47c6-8c31-7f8255e97eb3.jpg.280x210.jpg" alt="邻地铁+交通便利+配备齐全+精装修一室半" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100744374.html" title="邻地铁+交通便利+配备齐全+精装修一室半">邻地铁+交通便利+配备齐全+精装修一室半</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000017294/" class="laisuzhou"><span class="region">三义坊&nbsp;&nbsp;</span></a><span class="zone"><span>1室0厅&nbsp;&nbsp;</span></span><span class="meters">36.02平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/jingansi/">静安寺租房</a><span>/</span>低楼层(共7层)<span>/</span>1989年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span><span class="haskey"></span><span class="haskey-ex"><span>随时看房</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">4800</span>元/月</div><div class="price-pre">2018.12.06 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="10" data-log_index="10" data-id="107100534673" data-el="zufang" data-housecode="107100534673" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100534673.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/shfdfs-image/20171019/513cd7d7-b98b-42be-876b-5966a41a5592.jpg.280x210.jpg" alt="泰晤士维一精装独栋出租 地段好 户型霸气 大花园" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100534673.html" title="泰晤士维一精装独栋出租 地段好 户型霸气 大花园">泰晤士维一精装独栋出租 地段好 户型霸气 大花园</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000017221/" class="laisuzhou"><span class="region">泰晤士小镇(别墅)&nbsp;&nbsp;</span></a><span class="zone"><span>4室2厅&nbsp;&nbsp;</span></span><span class="meters">432.53平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/songjiangxincheng/">松江新城租房</a><span>/</span>低楼层(共3层)<span>/</span>2007年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="haskey"></span><span class="haskey-ex"><span>随时看房</span></span><span class="decoration"></span><span class="decoration-ex"><span>精装修</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">25000</span>元/月</div><div class="price-pre">2018.12.05 更新</div></div><div class="col-2"><div class="square"><div><span class="num">2</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="11" data-log_index="11" data-id="107100808300" data-el="zufang" data-housecode="107100808300" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100808300.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/c9d5129e-1b28-4b63-bb94-d7542d96fdd0.jpg.280x210.jpg" alt="九号线七宝站710米，万兆家园精装两房，房东诚意出租" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100808300.html" title="九号线七宝站710米，万兆家园精装两房，房东诚意出租">九号线七宝站710米，万兆家园精装两房，房东诚意出租</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000014319/" class="laisuzhou"><span class="region">万兆家园(二期)(公寓)&nbsp;&nbsp;</span></a><span class="zone"><span>3室2厅&nbsp;&nbsp;</span></span><span class="meters">100.44平米&nbsp;&nbsp;</span><span>南 北</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/qibao/">七宝租房</a><span>/</span>高楼层(共5层)<span>/</span>2002年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">8500</span>元/月</div><div class="price-pre">2018.12.06 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="12" data-log_index="12" data-id="107100793476" data-el="zufang" data-housecode="107100793476" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100793476.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/8eca4007-aa83-473c-a08a-555f4b84913b.jpg.280x210.jpg" alt="陆家嘴滨江精装两房 拎包即住 视野开阔" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100793476.html" title="陆家嘴滨江精装两房 拎包即住 视野开阔">陆家嘴滨江精装两房 拎包即住 视野开阔</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000002442/" class="laisuzhou"><span class="region">陆家嘴滨江公馆&nbsp;&nbsp;</span></a><span class="zone"><span>1室1厅&nbsp;&nbsp;</span></span><span class="meters">50平米&nbsp;&nbsp;</span><span>东南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/yangjing/">洋泾租房</a><span>/</span>中楼层(共29层)<span>/</span>1994年建塔楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="decoration"></span><span class="decoration-ex"><span>精装修</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">5900</span>元/月</div><div class="price-pre">2018.12.04 更新</div></div><div class="col-2"><div class="square"><div><span class="num">1</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="13" data-log_index="13" data-id="107100793380" data-el="zufang" data-housecode="107100793380" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100793380.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/19e2dd99-cbfc-4ddc-824f-1a6ed4268b1d.jpg.280x210.jpg" alt="宝地东花园 3室2厅 16000元" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/e0a6b5a6-885b-40bd-ada0-bb686a20168e.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100793380.html" title="宝地东花园 3室2厅 16000元">宝地东花园 3室2厅 16000元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000015846/" class="laisuzhou"><span class="region">宝地东花园&nbsp;&nbsp;</span></a><span class="zone"><span>3室2厅&nbsp;&nbsp;</span></span><span class="meters">120平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/zhoujiazuilu/">周家嘴路租房</a><span>/</span>低楼层(共25层)<span>/</span>板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">16000</span>元/月</div><div class="price-pre">2018.11.25 更新</div></div><div class="col-2"><div class="square"><div><span class="num">2</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="14" data-log_index="14" data-id="107100800189" data-el="zufang" data-housecode="107100800189" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100800189.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/30ee973f-49ed-4208-9fcb-94fff20d00e0.jpg.280x210.jpg" alt="银都名庭 2室0厅 7000元" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100800189.html" title="银都名庭 2室0厅 7000元">银都名庭 2室0厅 7000元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000017481/" class="laisuzhou"><span class="region">银都名庭&nbsp;&nbsp;</span></a><span class="zone"><span>2室0厅&nbsp;&nbsp;</span></span><span class="meters">75平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/caoyang/">曹杨租房</a><span>/</span>中楼层(共8层)<span>/</span>2002年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">7000</span>元/月</div><div class="price-pre">2018.12.06 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="15" data-log_index="15" data-id="107100805370" data-el="zufang" data-housecode="107100805370" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100805370.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/c3d61d86-7acb-4f98-a97a-e2950b76d08d.jpg.280x210.jpg" alt="三湘海尚城(公寓) 2室2厅 6500元" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100805370.html" title="三湘海尚城(公寓) 2室2厅 6500元">三湘海尚城(公寓) 2室2厅 6500元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000010638/" class="laisuzhou"><span class="region">三湘海尚城(公寓)&nbsp;&nbsp;</span></a><span class="zone"><span>2室2厅&nbsp;&nbsp;</span></span><span class="meters">88.05平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/songnan/">淞南租房</a><span>/</span>中楼层(共18层)<span>/</span>2012年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"></div></div></div></div><div class="col-3"><div class="price"><span class="num">6500</span>元/月</div><div class="price-pre">2018.12.04 更新</div></div><div class="col-2"><div class="square"><div><span class="num">1</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="16" data-log_index="16" data-id="107100766019" data-el="zufang" data-housecode="107100766019" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100766019.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/c5f3ee01-d119-47db-be23-42f24c6ef224.jpg.280x210.jpg" alt="地铁边 精装修 拎包即住 房东诚意出租" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/2a4d0e75-46be-47f7-8054-2b6eca2e2d42.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100766019.html" title="地铁边 精装修 拎包即住 房东诚意出租">地铁边 精装修 拎包即住 房东诚意出租</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000018230/" class="laisuzhou"><span class="region">江南名庐&nbsp;&nbsp;</span></a><span class="zone"><span>3室2厅&nbsp;&nbsp;</span></span><span class="meters">132.09平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/wuning/">武宁租房</a><span>/</span>中楼层(共33层)<span>/</span>2005年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">13000</span>元/月</div><div class="price-pre">2018.11.28 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="17" data-log_index="17" data-id="107100797817" data-el="zufang" data-housecode="107100797817" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100797817.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/905b678c-7447-4204-b83a-667fdc958aa7.jpg.280x210.jpg" alt="控江二村 1室1厅 4900元" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100797817.html" title="控江二村 1室1厅 4900元">控江二村 1室1厅 4900元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000017067/" class="laisuzhou"><span class="region">控江二村&nbsp;&nbsp;</span></a><span class="zone"><span>1室1厅&nbsp;&nbsp;</span></span><span class="meters">43.61平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/kongjianglu/">控江路租房</a><span>/</span>中楼层(共5层)<span>/</span>1975年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">4900</span>元/月</div><div class="price-pre">2018.11.24 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="18" data-log_index="18" data-id="107100787499" data-el="zufang" data-housecode="107100787499" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100787499.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/3b126aab-e13d-41ce-9686-4731d854767f.jpg.280x210.jpg" alt="陆家嘴精致一房，价格好谈，一线高区江景房" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/03800ddf-d0ce-45f5-8da6-b5a4923dd258.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100787499.html" title="陆家嘴精致一房，价格好谈，一线高区江景房">陆家嘴精致一房，价格好谈，一线高区江景房</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000016848/" class="laisuzhou"><span class="region">家化滨江苑&nbsp;&nbsp;</span></a><span class="zone"><span>1室2厅&nbsp;&nbsp;</span></span><span class="meters">85.3平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/tangqiao/">塘桥租房</a><span>/</span>高楼层(共33层)<span>/</span>2004年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span><span class="haskey"></span><span class="haskey-ex"><span>随时看房</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">9200</span>元/月</div><div class="price-pre">2018.12.02 更新</div></div><div class="col-2"><div class="square"><div><span class="num">3</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="19" data-log_index="19" data-id="107100790695" data-el="zufang" data-housecode="107100790695" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100790695.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/shfdfs-image/20171229/7be21052-2400-4df9-8536-5659b06a8816.jpg.280x210.jpg" alt="嘉乐花园 5室2厅2卫 嘉罗公路 老城区 近塔城路仓场路" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100790695.html" title="嘉乐花园 5室2厅2卫 嘉罗公路 老城区 近塔城路仓场路">嘉乐花园 5室2厅2卫 嘉罗公路 老城区 近塔城路仓场路</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000000502/" class="laisuzhou"><span class="region">嘉乐花园&nbsp;&nbsp;</span></a><span class="zone"><span>5室2厅&nbsp;&nbsp;</span></span><span class="meters">120平米&nbsp;&nbsp;</span><span>南 北</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/xinchenglu1/">新成路租房</a><span>/</span>高楼层(共6层)<span>/</span>1999年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="decoration"></span><span class="decoration-ex"><span>精装修</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">4600</span>元/月</div><div class="price-pre">2018.12.02 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="20" data-log_index="20" data-id="107100143709" data-el="zufang" data-housecode="107100143709" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100143709.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/rsp_pic_uploada9e2c2d3-1646-4830-9e99-8b0adb8d63e9.jpg.280x210.jpg" alt="2号线科技馆300米  世纪公园旁 自带会所 健身房游泳池" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100143709.html" title="2号线科技馆300米  世纪公园旁 自带会所 健身房游泳池">2号线科技馆300米  世纪公园旁 自带会所 健身房游泳池</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000016189/" class="laisuzhou"><span class="region">陆家嘴中央公寓&nbsp;&nbsp;</span></a><span class="zone"><span>2室2厅&nbsp;&nbsp;</span></span><span class="meters">130.69平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/yangdong/">杨东租房</a><span>/</span>中楼层(共25层)<span>/</span>2006年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">23000</span>元/月</div><div class="price-pre">2018.12.05 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="21" data-log_index="21" data-id="107100708061" data-el="zufang" data-housecode="107100708061" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100708061.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/test-89fcb6be-d5e2-4f85-8018-548d0df62b5d.png.280x210.jpg" alt="桃浦路191弄 2室1厅 5000元" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/test-5cf35864-1892-4c30-9e0c-cc1b21d4561d.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100708061.html" title="桃浦路191弄 2室1厅 5000元">桃浦路191弄 2室1厅 5000元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011102208458/" class="laisuzhou"><span class="region">桃浦路191弄&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">54.39平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/zhenru/">真如租房</a><span>/</span>中楼层(共6层)<span>/</span>1994年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">5000</span>元/月</div><div class="price-pre">2018.12.06 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="22" data-log_index="22" data-id="107100726939" data-el="zufang" data-housecode="107100726939" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100726939.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/a5b0cdc1-b3ec-46a9-9057-9105eaff7c74.jpg.280x210.jpg" alt="精装修，保养好，看房方便，地铁房，小区停车便利" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100726939.html" title="精装修，保养好，看房方便，地铁房，小区停车便利">精装修，保养好，看房方便，地铁房，小区停车便利</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000005480/" class="laisuzhou"><span class="region">湖畔天下&nbsp;&nbsp;</span></a><span class="zone"><span>3室2厅&nbsp;&nbsp;</span></span><span class="meters">113平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/nanxiang/">南翔租房</a><span>/</span>高楼层(共18层)<span>/</span>板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="haskey"></span><span class="haskey-ex"><span>随时看房</span></span><span class="decoration"></span><span class="decoration-ex"><span>精装修</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">5000</span>元/月</div><div class="price-pre">2018.12.02 更新</div></div><div class="col-2"><div class="square"><div><span class="num">4</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="23" data-log_index="23" data-id="107100804055" data-el="zufang" data-housecode="107100804055" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100804055.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/987a2fa7-7b5a-4c90-b739-c864758278f1.jpg.280x210.jpg" alt="上南五村 2室1厅 5200元" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/44dafed4-b3dc-457e-a918-ce5869a439d8.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100804055.html" title="上南五村 2室1厅 5200元">上南五村 2室1厅 5200元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000013710/" class="laisuzhou"><span class="region">上南五村&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">53.09平米&nbsp;&nbsp;</span><span>南 北</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/shibo/">世博租房</a><span>/</span>中楼层(共6层)<span>/</span>1987年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">5200</span>元/月</div><div class="price-pre">2018.12.06 更新</div></div><div class="col-2"><div class="square"><div><span class="num">9</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="24" data-log_index="24" data-id="107100807140" data-el="zufang" data-housecode="107100807140" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100807140.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/bd84ec9d-8ad9-4117-915b-2085e3ba89c6.jpg.280x210.jpg" alt="江桥一村 2室1厅 4200元" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100807140.html" title="江桥一村 2室1厅 4200元">江桥一村 2室1厅 4200元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000014535/" class="laisuzhou"><span class="region">江桥一村&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">74.55平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/jiangqiao/">江桥租房</a><span>/</span>中楼层(共6层)<span>/</span>1995年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"></div></div></div></div><div class="col-3"><div class="price"><span class="num">4200</span>元/月</div><div class="price-pre">2018.12.05 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="25" data-log_index="25" data-id="107100809942" data-el="zufang" data-housecode="107100809942" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100809942.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/e472eab0-b276-4ee8-82f0-839c1e214c58.jpg.280x210.jpg" alt="银杏小区 2室1厅 2100元" data-apart-layout="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100809942.html" title="银杏小区 2室1厅 2100元">银杏小区 2室1厅 2100元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000000354/" class="laisuzhou"><span class="region">银杏小区&nbsp;&nbsp;</span></a><span class="zone"><span>2室1厅&nbsp;&nbsp;</span></span><span class="meters">52.77平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/jiadinglaocheng/">嘉定老城租房</a><span>/</span>中楼层(共6层)<span>/</span>1990年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"></div></div></div></div><div class="col-3"><div class="price"><span class="num">2100</span>元/月</div><div class="price-pre">2018.12.03 更新</div></div><div class="col-2"><div class="square"><div><span class="num">3</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="26" data-log_index="26" data-id="107100486877" data-el="zufang" data-housecode="107100486877" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100486877.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/01df0f46-be5f-4896-b95f-4eae8e5fa495.jpg.280x210.jpg" alt="春申景城湖滨晨运  大三房  有钥匙配套成熟  邻近地铁" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/eefffa07-992f-4f18-b3c1-3bb65c9d9d50.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100486877.html" title="春申景城湖滨晨运  大三房  有钥匙配套成熟  邻近地铁">春申景城湖滨晨运  大三房  有钥匙配套成熟  邻近地铁</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000003337/" class="laisuzhou"><span class="region">春申景城湖滨晨韵&nbsp;&nbsp;</span></a><span class="zone"><span>3室2厅&nbsp;&nbsp;</span></span><span class="meters">127.5平米&nbsp;&nbsp;</span><span>南 北</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/chunshen/">春申租房</a><span>/</span>中楼层(共16层)<span>/</span>2005年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="decoration"></span><span class="decoration-ex"><span>精装修</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">7500</span>元/月</div><div class="price-pre">2018.12.01 更新</div></div><div class="col-2"><div class="square"><div><span class="num">3</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="27" data-log_index="27" data-id="107100544862" data-el="zufang" data-housecode="107100544862" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100544862.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/60d34557-6858-4eff-baab-c8369d085bb6.jpg.280x210.jpg" alt="古北国际广场 1室2厅 15500元" data-apart-layout="https://image1.ljcdn.com/x-se/shfdfs-image/20141203/cea2c137-265b-4ff9-82ff-2fcf0e5a4eb0.jpg.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100544862.html" title="古北国际广场 1室2厅 15500元">古北国际广场 1室2厅 15500元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000017080/" class="laisuzhou"><span class="region">古北国际广场&nbsp;&nbsp;</span></a><span class="zone"><span>1室2厅&nbsp;&nbsp;</span></span><span class="meters">78.09平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/gubei/">古北租房</a><span>/</span>低楼层(共32层)<span>/</span>2006年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">15500</span>元/月</div><div class="price-pre">2018.11.27 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="28" data-log_index="28" data-id="107100798087" data-el="zufang" data-housecode="107100798087" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100798087.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"  data-img="https://image1.ljcdn.com/310000-inspection/e652479e-6063-465e-a9fc-faff3c5a1db8.jpg.280x210.jpg" alt="菜花泾小区精装两房家具家电全配小区门口菜场近沃尔玛" data-apart-layout="https://image1.ljcdn.com/x-se/hdic-frame/7d070919-9f34-40bb-a4f4-10f3e91cea2f.png.280x210.jpg" /></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100798087.html" title="菜花泾小区精装两房家具家电全配小区门口菜场近沃尔玛">菜花泾小区精装两房家具家电全配小区门口菜场近沃尔玛</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5016389543047482/" class="laisuzhou"><span class="region">乐都路71号&nbsp;&nbsp;</span></a><span class="zone"><span>3室1厅&nbsp;&nbsp;</span></span><span class="meters">70平米&nbsp;&nbsp;</span><span>南</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/songjianglaocheng/">松江老城租房</a><span>/</span>高楼层(共6层)<span>/</span>1990年建板楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">3000</span>元/月</div><div class="price-pre">2018.12.05 更新</div></div><div class="col-2"><div class="square"><div><span class="num">1</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li><li data-index="29" data-log_index="29" data-id="107100540313" data-el="zufang" data-housecode="107100540313" data-is_focus="" data-sl=""><div class="pic-panel"><a target="_blank" href="https://sh.lianjia.com/zufang/107100540313.html"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/new-version/default_block.png?_v=20181206222953"></a></div><div class="info-panel"><h2><a target="_blank" href="https://sh.lianjia.com/zufang/107100540313.html" title="华美达酒店式公寓 1房间1卫 3800元">华美达酒店式公寓 1房间1卫 3800元</a></h2><div class="col-1"><div class="where"><a href="https://sh.lianjia.com/xiaoqu/5011000000549/" class="laisuzhou"><span class="region">华美达酒店式公寓&nbsp;&nbsp;</span></a><span class="zone"><span>1室0厅&nbsp;&nbsp;</span></span><span class="meters">36.54平米&nbsp;&nbsp;</span><span>北</span></div><div class="other"><div class="con"><a href="https://sh.lianjia.com/zufang/huangxinggongyuan/">黄兴公园租房</a><span>/</span>高楼层(共21层)<span>/</span>2008年建塔楼</div></div><div class="chanquan"><div class="left agency"><div class="view-label left"><span class="fang-subway"></span><span class="fang-subway-ex"><span>近地铁</span></span></div></div></div></div><div class="col-3"><div class="price"><span class="num">3800</span>元/月</div><div class="price-pre">2018.11.25 更新</div></div><div class="col-2"><div class="square"><div><span class="num">0</span>人</div><div class="col-look">看过此房</div></div></div><!--<div class="view"><span class="view-map">预览地图</span><span class="notice-focus" data-id=""></span><a class="view-del" target="_blank" href="" title=""></a></div>--></div></li></ul><div style="display:none;"></div>
<div class="page-box house-lst-page-box" comp-module='page' page-url="/zufang/pg{page}/"page-data='{"totalPage":100,"curPage":1}'></div>


</div></div><!-- <div id="list-side" class="side-bar" style="display:none;"><div id="map-box" class="map-box"></div><div class="search-widget"><form action=""><input type="text" class="txt" placeholder="搜哪儿去哪儿！" /><input type="submit" value="" class="btn" /></form></div></div> --></div><!--  <div class="recommend" id="rec-dom" style="display:none"><div class="hd clear"><h5>热门小区推荐</h5></div><div class="recommend-lst clear"></div></div> -->
</div>

<div class="pagination_group_a">
      <a href="/zufang/"></a>
      <a href="/zufang/pg2/"></a>
      <a href="/zufang/pg3/"></a>
      <a href="/zufang/pg4/"></a>
      <a href="/zufang/pg5/"></a>
      <a href="/zufang/pg6/"></a>
      <a href="/zufang/pg7/"></a>
      <a href="/zufang/pg8/"></a>
      <a href="/zufang/pg9/"></a>
      <a href="/zufang/pg10/"></a>
  </div>
 <script type="text/template" id="sem_card_tpl" semResblockId="">

      <div class="agentCardPush LOGVIEW" log-mod="zufang_list_semcard" data-bl="agent" data-el="<%=data.agentUcid%>" data-log_id="20001" data-log_value="<%=data.resblockId%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>">
        <div class="agentCardAgentInfo">
          <a href="<%=data.agentUrl%>" target="_blank" class="agentCardAgentImg LOGCLICK" data-bl="agent"  data-log_value="<%=data.resblockId%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>"><img src="<%=data.photoPath%>.75x100.jpg" alt="小区顾问"></a>
          <div class="cardAgentInfo">
            <div class="cardAgentNameContainer im-talk"><a target="_blank" href="<%=data.agentUrl%>" class="cardAgentName LOGCLICK" data-bl="agent"  data-log_value="<%=data.resblockId%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>"><%=data.name%></a><a class="cardAgentIM LOGCLICK im-talk" data-bl="agent_im" data-ucid="<%=data.agentUcid%>"  data-source-port="PC:ershou_zufang_list_top" data-source-extends=<%=JSON.stringify(communityId)%>></a><span class="cardAgentTitle">置业顾问</span></div>
            <div class="cardAgentPhone"><%=data.fourPhoneOne%></div>
            <div class="cardAgentDesc"><%=data.desc%></div>
          </div>
        </div>
        <div class="agentCardResblockInfo">
          <div class="agentCardResblockName">
            <a class="agentCardResblockTitle LOGCLICK" data-bl="agent_resblock_name"  data-log_value="<%=data.resblockId%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>" target="_blank" href="<%=data.resblockUrl%>"><%=data.resblockName%></a>
            <span class="agentCardResblockSubTitle"><%=data.districtName%><%=data.bizcircleName%></span>
            <a href="<%=data.resblockUrl%>" target="_blank" class="agentCardResblockLink LOGCLICK" data-bl="agent_resblock_info"  data-log_value="<%=data.resblockId%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>">查看小区详情</a>
          </div>
          <div class="agentCardResblockDetail">
            <div class="agentCardDetailItem">
              <div class="agentCardDetailTitle">小区租金</div>
              <a href="<%=data.fangjiaUrl%>" target="_blank" class="agentCardDetailInfo LOGCLICK" data-bl="agent_resblock_avg" data-log_value="<%=data.resblockId%>" data-log_source="<%=data.ljwebSource%>" data-log_statId="<%=data.ljwebStatId%>">
              <%if (data.unitPrice != '暂无'){%>
              <%=data.unitPrice%>元/月
              <%}else{%>
                暂无
              <%}%>
              </a>
            </div>
            <div class="agentCardDetailItem">
              <div class="agentCardDetailTitle">正在出租</div>
              <div class="agentCardDetailInfo"><%=data.sellNum%>套</div>
            </div>
            <div class="agentCardDetailItem">
              <div class="agentCardDetailTitle">近90天成交</div>
              <div class="agentCardDetailInfo"><%=data['90saleCount']%>套</div>
            </div>
            <div class="agentCardDetailItem">
              <div class="agentCardDetailTitle">近30天带看</div>
              <div class="agentCardDetailInfo"><%=data.day30See%>次</div>
            </div>
          </div>
        </div>
      </div>

</script>
<div class="footer"><div class="wrapper"><div class="f-title"><div class="fl"><ul><li><a href="https://www.lianjia.com/zhuanti/home/" rel="nofollow" target="_blank">了解链家</a></li><li><a href="https://sh.lianjia.com/about/aboutlianjia/" rel="nofollow" target="_blank">关于链家</a></li><li><a href="https://sh.lianjia.com/about/contactus/" rel="nofollow" target="_blank">联系我们</a></li><li><a href="http://join.lianjia.com/" rel="nofollow" target="_blank">加入我们</a></li><li><a href="https://www.lianjia.com/privacy/" rel="nofollow" target="_blank">隐私声明</a></li><li><a href="https://sh.lianjia.com/sitemap/" target="_blank">网站地图</a></li><li><a href="https://page.lianjia.com/subject/youlian.html" rel="nofollow" target="_blank">友情链接</a></li><li><a href="https://agent.lianjia.com/" rel="nofollow" target="_blank">经纪人登录</a></li></ul></div><div class="fr">官方客服 1010 9666</div></div><div class="lianjia-link-box"><div class="fl"><div class="tab"><span  class="hover">城市二手房</span><span >房产资讯</span><span >城区二手房</span><span >城区租房</span><span >城区小区</span><span >热门小区</span><span >热门问答</span><span >热门百科</span><span >合作与友情链接</span></div><div class="link-list"><div><dd><a target="_blank" href="https://bj.lianjia.com/">北京房产网</a><a target="_blank" href="https://sh.lianjia.com/">上海房产网</a><a target="_blank" href="https://gz.lianjia.com/">广州房产网</a><a target="_blank" href="https://sz.lianjia.com/">深圳房产网</a><a target="_blank" href="https://tj.lianjia.com/">天津房产网</a><a target="_blank" href="https://cd.lianjia.com/">成都房产网</a><a target="_blank" href="https://nj.lianjia.com/">南京房产网</a><a target="_blank" href="https://hz.lianjia.com/">杭州房产网</a><a target="_blank" href="https://qd.lianjia.com/">青岛房产网</a><a target="_blank" href="https://dl.lianjia.com/">大连房产网</a><a target="_blank" href="https://su.lianjia.com/">苏州房产网</a><a target="_blank" href="https://xm.lianjia.com/">厦门房产网</a><a target="_blank" href="https://wh.lianjia.com/">武汉房产网</a><a target="_blank" href="https://cq.lianjia.com/">重庆房产网</a><a target="_blank" href="https://cs.lianjia.com/">长沙房产网</a><a target="_blank" href="https://jn.lianjia.com/">济南房产网</a><a target="_blank" href="https://fs.lianjia.com/">佛山房产网</a><a target="_blank" href="https://dg.lianjia.com/">东莞房产网</a><a target="_blank" href="https://xa.lianjia.com/">西安房产网</a><a target="_blank" href="https://sjz.lianjia.com/">石家庄房产网</a><a target="_blank" href="https://yt.lianjia.com/">烟台房产网</a><a target="_blank" href="https://wz.lianjia.com/">温州房产网</a><a target="_blank" href="https://zs.lianjia.com/">中山房产网</a><a target="_blank" href="https://zh.lianjia.com/">珠海房产网</a><a target="_blank" href="https://jx.lianjia.com/">嘉兴房产网</a><a target="_blank" href="https://hui.lianjia.com/">惠州房产网</a><a target="_blank" href="https://ty.lianjia.com/">太原房产网</a><a target="_blank" href="https://sy.lianjia.com/">沈阳房产网</a><a target="_blank" href="https://nt.lianjia.com/">南通房产网</a><a target="_blank" href="https://hk.lianjia.com/">海口房产网</a><a target="_blank" href="https://wf.lianjia.com/">潍坊房产网</a><a target="_blank" href="https://linyi.lianjia.com/">临沂房产网</a><a target="_blank" href="https://wx.lianjia.com/">无锡房产网</a><a target="_blank" href="https://san.lianjia.com/">三亚房产网</a><a target="_blank" href="https://lf.lianjia.com/">廊坊房产网</a><a target="_blank" href="https://hf.lianjia.com/">合肥房产网</a><a target="_blank" href="https://km.lianjia.com/">昆明房产网</a><a target="_blank" href="https://zz.lianjia.com/">郑州房产网</a><a target="_blank" href="https://quanzhou.lianjia.com/">泉州房产网</a><a target="_blank" href="https://zj.lianjia.com/">镇江房产网</a><a target="_blank" href="https://qy.lianjia.com/">清远房产网</a><a target="_blank" href="https://sx.lianjia.com/">绍兴房产网</a><a target="_blank" href="https://weihai.lianjia.com/">威海房产网</a><a target="_blank" href="https://zhangzhou.lianjia.com/">漳州房产网</a><a target="_blank" href="https://cc.lianjia.com/">长春房产网</a><a target="_blank" href="https://gy.lianjia.com/">贵阳房产网</a><a target="_blank" href="https://hhht.lianjia.com/">呼和浩特房产网</a><a target="_blank" href="https://changde.lianjia.com/">常德房产网</a><a target="_blank" href="https://sr.lianjia.com/">上饶房产网</a><a target="_blank" href="https://fz.lianjia.com/">福州房产网</a><a target="_blank" href="https://zhuzhou.lianjia.com/">株洲房产网</a><a target="_blank" href="https://yinchuan.lianjia.com/">银川房产网</a><a target="_blank" href="https://bh.lianjia.com/">北海房产网</a><a target="_blank" href="https://xianyang.lianjia.com/">咸阳房产网</a><a target="_blank" href="https://ha.lianjia.com/">淮安房产网</a><a target="_blank" href="https://mianyang.lianjia.com/">绵阳房产网</a><a target="_blank" href="https://dazhou.lianjia.com/">达州房产网</a><a target="_blank" href="https://xinxiang.lianjia.com/">新乡房产网</a><a target="_blank" href="https://nanchong.lianjia.com/">南充房产网</a><a target="_blank" href="https://luoyang.lianjia.com/">洛阳房产网</a><a target="_blank" href="https://zhanjiang.lianjia.com/">湛江房产网</a><a target="_blank" href="https://nc.lianjia.com/">南昌房产网</a><a target="_blank" href="https://huangshi.lianjia.com/">黄石房产网</a><a target="_blank" href="https://xy.lianjia.com/">襄阳房产网</a><a target="_blank" href="https://zb.lianjia.com/">淄博房产网</a><a target="_blank" href="https://kf.lianjia.com/">开封房产网</a><a target="_blank" href="https://yichang.lianjia.com/">宜昌房产网</a><a target="_blank" href="https://nb.lianjia.com/">宁波房产网</a><a target="_blank" href="https://xc.lianjia.com/">许昌房产网</a><a target="_blank" href="https://hrb.lianjia.com/">哈尔滨房产网</a><a target="_blank" href="https://changzhou.lianjia.com/">常州房产网</a><a target="_blank" href="https://jiangmen.lianjia.com/">江门房产网</a><a target="_blank" href="https://lz.lianjia.com/">兰州房产网</a><a target="_blank" href="https://liuzhou.lianjia.com/">柳州房产网</a><a target="_blank" href="https://mas.lianjia.com/">马鞍山房产网</a><a target="_blank" href="https://dd.lianjia.com/">丹东房产网</a><a target="_blank" href="https://gl.lianjia.com/">桂林房产网</a><a target="_blank" href="https://huzhou.lianjia.com/">湖州房产网</a><a target="_blank" href="https://yc.lianjia.com/">盐城房产网</a><a target="_blank" href="https://taizhou.lianjia.com/">台州房产网</a><a target="_blank" href="https://hanzhong.lianjia.com/">汉中房产网</a><a target="_blank" href="https://liangshan.lianjia.com/">凉山房产网</a><a target="_blank" href="https://jh.lianjia.com/">金华房产网</a><a target="_blank" href="https://nn.lianjia.com/">南宁房产网</a><a target="_blank" href="https://wuhu.lianjia.com/">芜湖房产网</a><a target="_blank" href="https://jl.lianjia.com/">吉林房产网</a><a target="_blank" href="https://aq.lianjia.com/">安庆房产网</a><a target="_blank" href="https://ganzhou.lianjia.com/">赣州房产网</a><a target="_blank" href="https://baoji.lianjia.com/">宝鸡房产网</a><a target="_blank" href="https://jian.lianjia.com/">吉安房产网</a></dd></div><div><dd><a target="_blank" href="https://news.lianjia.com/">房产资讯</a><a target="_blank" href="https://news.lianjia.com/bj/">北京房产资讯</a><a target="_blank" href="https://news.lianjia.com/bj/baike/">北京房产百科</a><a target="_blank" href="https://bj.lianjia.com/wenda/">北京房产知识</a><a target="_blank" href="https://news.lianjia.com/sh/">上海房产资讯</a><a target="_blank" href="https://news.lianjia.com/sh/baike/">上海房产百科</a><a target="_blank" href="https://sh.lianjia.com/wenda/">上海房产知识</a><a target="_blank" href="https://news.lianjia.com/gz/">广州房产资讯</a><a target="_blank" href="https://news.lianjia.com/gz/baike/">广州房产百科</a><a target="_blank" href="https://gz.lianjia.com/wenda/">广州房产知识</a><a target="_blank" href="https://news.lianjia.com/sz/">深圳房产资讯</a><a target="_blank" href="https://news.lianjia.com/sz/baike/">深圳房产百科</a><a target="_blank" href="https://sz.lianjia.com/wenda/">深圳房产知识</a><a target="_blank" href="https://news.lianjia.com/tj/">天津房产资讯</a><a target="_blank" href="https://news.lianjia.com/tj/baike/">天津房产百科</a><a target="_blank" href="https://tj.lianjia.com/wenda/">天津房产知识</a><a target="_blank" href="https://news.lianjia.com/cd/">成都房产资讯</a><a target="_blank" href="https://news.lianjia.com/cd/baike/">成都房产百科</a><a target="_blank" href="https://cd.lianjia.com/wenda/">成都房产知识</a><a target="_blank" href="https://news.lianjia.com/nj/">南京房产资讯</a><a target="_blank" href="https://news.lianjia.com/nj/baike/">南京房产百科</a><a target="_blank" href="https://nj.lianjia.com/wenda/">南京房产知识</a><a target="_blank" href="https://news.lianjia.com/hz/">杭州房产资讯</a><a target="_blank" href="https://news.lianjia.com/hz/baike/">杭州房产百科</a><a target="_blank" href="https://hz.lianjia.com/wenda/">杭州房产知识</a><a target="_blank" href="https://news.lianjia.com/qd/">青岛房产资讯</a><a target="_blank" href="https://news.lianjia.com/qd/baike/">青岛房产百科</a><a target="_blank" href="https://qd.lianjia.com/wenda/">青岛房产知识</a><a target="_blank" href="https://news.lianjia.com/dl/">大连房产资讯</a><a target="_blank" href="https://news.lianjia.com/dl/baike/">大连房产百科</a><a target="_blank" href="https://dl.lianjia.com/wenda/">大连房产知识</a><a target="_blank" href="https://news.lianjia.com/su/">苏州房产资讯</a><a target="_blank" href="https://news.lianjia.com/su/baike/">苏州房产百科</a><a target="_blank" href="https://su.lianjia.com/wenda/">苏州房产知识</a><a target="_blank" href="https://news.lianjia.com/xm/">厦门房产资讯</a><a target="_blank" href="https://news.lianjia.com/xm/baike/">厦门房产百科</a><a target="_blank" href="https://news.lianjia.com/wh/">武汉房产资讯</a><a target="_blank" href="https://news.lianjia.com/wh/baike/">武汉房产百科</a><a target="_blank" href="https://news.lianjia.com/cq/">重庆房产资讯</a><a target="_blank" href="https://news.lianjia.com/cq/baike/">重庆房产百科</a><a target="_blank" href="https://cq.lianjia.com/wenda/">重庆房产知识</a><a target="_blank" href="https://news.lianjia.com/cs/">长沙房产资讯</a><a target="_blank" href="https://news.lianjia.com/cs/baike/">长沙房产百科</a><a target="_blank" href="https://cs.lianjia.com/wenda/">长沙房产知识</a><a target="_blank" href="https://news.lianjia.com/jn/">济南房产资讯</a><a target="_blank" href="https://news.lianjia.com/jn/baike/">济南房产百科</a><a target="_blank" href="https://jn.lianjia.com/wenda/">济南房产知识</a><a target="_blank" href="https://news.lianjia.com/fs/">佛山房产资讯</a><a target="_blank" href="https://news.lianjia.com/fs/baike/">佛山房产百科</a><a target="_blank" href="https://fs.lianjia.com/wenda/">佛山房产知识</a><a target="_blank" href="https://news.lianjia.com/dg/">东莞房产资讯</a><a target="_blank" href="https://news.lianjia.com/dg/baike/">东莞房产百科</a><a target="_blank" href="https://dg.lianjia.com/wenda/">东莞房产知识</a><a target="_blank" href="https://news.lianjia.com/xa/">西安房产资讯</a><a target="_blank" href="https://news.lianjia.com/xa/baike/">西安房产百科</a><a target="_blank" href="https://xa.lianjia.com/wenda/">西安房产知识</a><a target="_blank" href="https://news.lianjia.com/sjz/">石家庄房产资讯</a><a target="_blank" href="https://news.lianjia.com/sjz/baike/">石家庄房产百科</a><a target="_blank" href="https://sjz.lianjia.com/wenda/">石家庄房产知识</a><a target="_blank" href="https://news.lianjia.com/yt/">烟台房产资讯</a><a target="_blank" href="https://news.lianjia.com/yt/baike/">烟台房产百科</a><a target="_blank" href="https://news.lianjia.com/sy/">沈阳房产资讯</a><a target="_blank" href="https://news.lianjia.com/sy/baike/">沈阳房产百科</a><a target="_blank" href="https://sy.lianjia.com/wenda/">沈阳房产知识</a><a target="_blank" href="https://news.lianjia.com/hf/">合肥房产资讯</a><a target="_blank" href="https://news.lianjia.com/hf/baike/">合肥房产百科</a><a target="_blank" href="https://hf.lianjia.com/wenda/">合肥房产知识</a><a target="_blank" href="https://news.lianjia.com/zz/">郑州房产资讯</a><a target="_blank" href="https://news.lianjia.com/zz/baike/">郑州房产百科</a></dd></div><div><dd><a target="_blank" href="https://sh.lianjia.com/ershoufang/shanghaizhoubian/">上海周边二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/jiading/">嘉定二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/fengxian/">奉贤二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/baoshan/">宝山二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/chongming/">崇明二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/xuhui/">徐汇二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/putuo/">普陀二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/yangpu/">杨浦二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/songjiang/">松江二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/pudong/">浦东二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/haiwai/">海外二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/hongkou/">虹口二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/jinshan/">金山二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/changning/">长宁二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/minhang/">闵行二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/zhabei/">闸北二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/qingpu/">青浦二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/jingan/">静安二手房</a><a target="_blank" href="https://sh.lianjia.com/ershoufang/huangpu/">黄浦二手房</a></dd></div><div><dd><a target="_blank" href="https://sh.lianjia.com/zufang/shanghaizhoubian/">上海周边租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/jiading/">嘉定租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/fengxian/">奉贤租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/baoshan/">宝山租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/chongming/">崇明租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/xuhui/">徐汇租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/putuo/">普陀租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/yangpu/">杨浦租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/songjiang/">松江租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/pudong/">浦东租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/haiwai/">海外租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/hongkou/">虹口租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/jinshan/">金山租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/changning/">长宁租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/minhang/">闵行租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/zhabei/">闸北租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/qingpu/">青浦租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/jingan/">静安租房</a><a target="_blank" href="https://sh.lianjia.com/zufang/huangpu/">黄浦租房</a></dd></div><div><dd><a target="_blank" href="https://sh.lianjia.com/xiaoqu/shanghaizhoubian/">上海周边小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/jiading/">嘉定小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/fengxian/">奉贤小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/baoshan/">宝山小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/chongming/">崇明小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/xuhui/">徐汇小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/putuo/">普陀小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/yangpu/">杨浦小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/songjiang/">松江小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/pudong/">浦东小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/haiwai/">海外小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/hongkou/">虹口小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/jinshan/">金山小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/changning/">长宁小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/minhang/">闵行小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/zhabei/">闸北小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/qingpu/">青浦小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/jingan/">静安小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/huangpu/">黄浦小区</a></dd></div><div><dd><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017985/">金江家园</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017245/">金汇华光城</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000014845/">新顾村大家园C区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000006255/">航东路750弄</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000002055/">民星路408弄</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017867/">广灵二村</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017670/">金鹏苑</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000015967/">信和花园</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000004603/">殷行路430弄</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000012194/">市民新村</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000014998/">日晖六村</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000003419/">汇智湖畔家园</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017500/">中大丽都</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000014566/">宝北小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000016478/">瀚林世家</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000010607/">江诚苑</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000016508/">东方明珠大宁公寓</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017106/">阳光威尼斯(四期)(公寓)</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000014715/">荣欣苑</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000007616/">法华镇路101弄</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017248/">嘉茵苑</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000001588/">象屿大宁悦府</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000004942/">申云小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5016389543047188/">上海派</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000008870/">长隆住宅小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000010649/">泰山一村</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000003545/">花园城</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000010005/">民星住宅小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000006328/">建设新村</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000010191/">欣兰苑</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000019275/">复兴珑御</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000002708/">晨星四季苑</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000012110/">狮城花苑</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000004473/">德都路165弄</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000014084/">振宏小区</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017044/">甘泉二村</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000020456/">中环国际公寓(二期)</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000015024/">金桂苑(徐汇)</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000017035/">旭丽花园</a><a target="_blank" href="https://sh.lianjia.com/xiaoqu/5011000004617/">锦杨苑</a></dd></div><div><dd><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b1001/">房价行情</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b1002/">购房建议</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b1003/">购房资质</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b1004/">买房风险</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b1005/">二手房</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b1006/">新房</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b1007/">海外买房</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b2001/">税费计算</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b2002/">认购签约</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b2003/">资金监管</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b2004/">过户流程</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b2005/">入住交接</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b3001/">房屋估价</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b3002/">卖房流程</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b3003/">出售方案</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b3004/">业主风险</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b3005/">卖旧买新</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b5001/">贷款利率</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b5002/">首付月供</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b5003/">贷款流程</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b5004/">住房公积金</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b5005/">商业贷款</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b5006/">融资借款</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b5007/">金融方案</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b6001/">房产政策</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b6002/">法律纠纷</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b6003/">保障住房</a><a target="_blank" href="https://sh.lianjia.com/wenda/liebiao/b6004/">其他</a></dd></div><div><dd><a target="_blank" href="https://news.lianjia.com/sh/baike/0033/">房产政策</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0035/">购房建议</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0036/">购房资质</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0037/">房屋贷款</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0039/">保障住房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0040/">产权/变更</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0041/">法律纠纷</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0042/">房屋装修</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0044/">准备买房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0045/">看房/选房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0046/">签约/定房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0047/">全款/贷款</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0048/">缴税/过户</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0049/">入住/交接</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0050/">买房风险</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0051/">准备买房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0052/">看房/选房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0053/">认购新房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0054/">签约/定房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0055/">全款/贷款</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0056/">收房/验房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0057/">装修/入住</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0058/">退房/维权</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0059/">各国概况</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0060/">计划买房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0061/">签约定房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0062/">银行贷款</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0063/">交易过户</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0064/">房屋代理</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0066/">准备卖房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0067/">产权核验</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0068/">收定金/签约</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0069/">分步收款</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0070/">缴税/过户</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0071/">交房须知</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0072/">卖房风险</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0073/">准备换房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0074/">换房方案</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0075/">卖旧/买新</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0077/">缴税/过户</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0078/">交房/收房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/0079/">换房风险</a><a target="_blank" href="https://news.lianjia.com/sh/baike/00779/">找房看房</a><a target="_blank" href="https://news.lianjia.com/sh/baike/00780/">签约付款</a><a target="_blank" href="https://news.lianjia.com/sh/baike/00781/">物业交割</a><a target="_blank" href="https://news.lianjia.com/sh/baike/00782/">租房纠纷</a><a target="_blank" href="https://news.lianjia.com/sh/baike/00783/">我是房东</a></dd></div><div><dd><a target="_blank" href="https://www.tujia.com/duanzu/sanming/">三明日租房</a></dd></div></div></div><div class="clear"></div></div><div class="bottom"><div class="copyright fl">链家网（北京）科技有限公司 | 网络经营许可证 京ICP备16057509号-2 | © Copyright©2010-2018 链家网Lianjia.com版权所有</div><div style="width:300px;color: #888c8e;font-size: 12px;line-height: 20px;"><a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802024019" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;"><img src="https://s1.ljcdn.com/feroot/pc/asset/img/home/beian.png?_v=20181206222953"" style="float:left;"><p style="float:left;height:20px;line-height:20px;margin: 0px 0px 0px 5px;color: #888c8e;">京公网安备 11010802024019号</p></a></div></div></div></div>

<script src="https://s1.ljcdn.com/feroot/pc/asset/base/fe.js?_v=20181206222953"></script><script src="https://s1.ljcdn.com/feroot/pc/asset/common/common.js?_v=20181206222953"></script><div style="display:none"><script src="https://s1.ljcdn.com/feroot/dep/ljanalytics.js?_v=20181206222953"></script></div><div id="only" data-city="sh" data-page="zufang_search"></div>

<script>var path = 'https://s1.ljcdn.com/feroot/pc/asset?_v=20181206222953'.split("?");require.config({baseUrl: path[0],paths: {'echarts' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/bar' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/line' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/pie' : '../../dep/echarts-1.4.1/build/echarts','echarts3' : '../../dep/echarts3/echarts3','common': 'common','jquery-ui': '../../dep/jquery-ui/jquery-ui.min','zeroclipboard': '../../dep/zeroclipboard-2.2.0/ZeroClipboard'},urlArgs:  path[1]});var feData = {"cityName": "北京","getFavHouseUrl":       "/api/gethousefav","setFavHouseUrl":       "/api/sethousefav","getLastSearch":        "/api/getlastsearch","getCommunityHistory":  "/api/getcommunityhistory","verifyHouse":          "/api/verifyHouse","getUser":              "/api/getUser","verifyCode":           "/verifycode/getVerifyCode","complaint":            "/api/complaint","getDecoration":        "/api/getDecoration","trendData" :           "/site/getpicinfo"}</script>
<script type="text/javascript">
require(['list/main'], function (main) {
    main.init({
        feRoot: 'https://s1.ljcdn.com/feroot/?_v=20181206222953',
        cityName: '上海',
        mapak: 'C106a48023d9606dcdad761cbc070095',
        mapDomId: 'map-box',
        reqData: {
            cityId: '310000'
        },

        common: feData,
        price: '/zufang/brp{min}erp{max}/',
        area: '/zufang/rba{min}rea{max}/',

        dingdingBox: ''
    });
});
require(['common/backtopV3'], function (main) {
  main({
    ucid: '',
    uuid: 'a7ad8b25-df36-4b00-8ab6-ac1f0fe123df',
    loadingImg: 'https://s1.ljcdn.com/feroot/pc/asset/ershoufang/sellDetail/img/loading.gif?_v=20181206222953',
    qrImg: '//ajax.api.lianjia.com/qr/getDownloadQr'
  });
});
require(['zufang/main'], function (main) {
    main.init({
        feRoot: 'https://s1.ljcdn.com/feroot/?_v=20181206222953',
        cityName: '上海',
        mapak: 'C106a48023d9606dcdad761cbc070095',
        mapDomId: 'map-box',
        reqData: {
            cityId: '310000'
        },

        common: feData,
        price: '/zufang/brp{min}erp{max}/',
        area: '/zufang/rba{min}rea{max}/',

        dingdingBox: ''
    });
});

require(['common/initTalk'], function(initTalk) {
  initTalk()
});

;;+function() {
    LjUserTrack.send({
        "ljweb_id": "10001",
        "ljweb_mod": "zufang_list_view",
        "ljweb_bl": "spk_0",
        "ljweb_el": "25787",
        "ljweb_value": "",
    });
    var isHaveAgentCard = false
    var clickLinkBl = 'list';
    var resblockId = '';
    if(isHaveAgentCard){
      clickLinkBl = 'list_have_sem_card';
      resblockId = ""
    }
    $(document.body).on("click", "[data-el='zufang']", function() {
        var $m = $(this);
        LjUserTrack.send({
            "ljweb_id": "10002",
            "ljweb_mod": "zufang_list_list",
            "ljweb_bl": clickLinkBl,
            "ljweb_el": "zufang",
            "ljweb_index": $m.attr("data-log_index"),
            "ljweb_url": $m.attr("href"),
            "ljweb_value":resblockId,
            "ljweb_is_focus" : $m.attr("data-is_focus") || 0,
            "ljweb_house_code" : $m.attr('data-housecode')
        });

    });

    $(document.body).on("mousedown", "#suggest-cont [data-log_value]", function() {
        var $m = $(this);
        var channel = $m.attr('data-log_channel');
        LjUserTrack.send({
            "ljweb_id": 10003,
            "ljweb_mod": channel+"_list_search",
            "ljweb_bl": "search",
            "ljweb_el": $m.attr("data-log_value"),
            "ljweb_index": $m.attr("data-log_index"),
            "ljweb_value": $.trim($("#keyword-box").val()),
            "ljweb_url": $m.attr("data-log_url")
        });
    });
    $(document.body).on("mousedown", ".hot-sug[data-bl='sug'] [data-log_value]", function() {
        var $m = $(this);
        var channel = $m.attr('data-log_channel');
        LjUserTrack.send({
            "ljweb_id": 10004,
            "ljweb_mod": channel+"_list_search",
            "ljweb_bl": "search",
            "ljweb_el": $m.attr("data-log_value"),
            "ljweb_index": $m.attr("data-log_index"),
            "ljweb_value": $.trim($("#keyword-box").val()),
            "ljweb_url": $m.attr("href")
        });
    });
    $("#searchForm").on("submit", function() {
        var $m = $(this);
        var channel = $m.find("[data-bl=switch][actdata]").attr('actdata') || 'zufang';
        LjUserTrack.send({
            "ljweb_id": "10008",
            "ljweb_mod": channel+"_list_search",
            "ljweb_bl": "search",
            "ljweb_value": $.trim($("#keyword-box").val())
        });
    });

}();
</script>

<!-- ｛include file='../common/toolbar.tpl'} -->
<script>require(['common/suggestion'], function (suggestion) {window.defaultSuggest = suggestion.init({requestOptions: {cityId: '310000',cityName: '上海'},url: '/api/headerSearch?channel=zufang&q=',main: '#keyword-box',appendTo: '#suggest-cont',redirect: true});});</script><div class="loninContaner"><div class="overlay_bg"></div><div class="panel_login animated" id="dialog"><div class="panel_info"><i class="close_login" >&times</i><div class="panel_tab"><div class="title"><div class="fl">账号密码登录</div></div><div class="clear"></div><div id="con_login_user"><form action="" method="post"><ul><li class="item border-t userName"><input type="text" class="the_input topSpecial users" placeholder="请输入手机号"  maxlength="11" /></li><li class="item border-b pwd"><input type="password" class="the_input password" maxlength="20" placeholder="请输入登录密码"/><em class="password-view"></em></li><li class="item checkVerimg" style="display:none;"><input type="text" class="the_input ver-img" maxlength="6"  placeholder="请输入验证码"/><img class="verImg"></li><li class="item drag" style="display:none;"><div id="drag"></div></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked/></span>7天内免登录</label><a href="javascript:;" rel="nofollow" class="toforget">忘记密码</a></li><li class="li_btn"><a class="login-user-btn"  />登录</a></li><li class="footer-link"><a href="javascript:;" rel="nofollow" class="totellogin">手机快捷登录</a></li></ul></form></div><div id="con_login_agent" class="undis"><form action="" method="post"><ul><li class="item"><dd></dd><input type="text" class="the_input users" placeholder="输入经纪人ID号码" /></li><li class="item"><input type="password" class="the_input password"  placeholder="登录密码"/></li><li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked/></span>7天内免登录</label><a href="https://passport.lianjia.com/register/resources/lianjia/forget.html?service=http://bj.lianjia.com/" rel="nofollow">忘记密码</a></li><li><input class="login-agent-btn" value="立即登录"/></li></ul></form></div></div></div><div class="registered"></div></div><div class="panel_login animated" id="dialog_tel"><div class="panel_info"><i class="close_login">&times</i><div class="panel_tab"><div class="title"><div class="fl">手机快捷登录</div><div class="register_text_tel">别担心，无账号自动注册不会导致手机号被泄露</div></div><div class="clear"></div><div id="con_login_user_tel"><form action="" method="post"><ul><li class="item border-t userName"><input type="text" class="the_input topSpecial users_tel" maxlength="11" placeholder="请输入手机号" /></li><!-- <li class="item pwd"><input type="password" class="the_input password_tel"  placeholder="请输入短信验证码"/></li> --><li class="item checkVerimg" style=""><input type="text" class="the_input ver-img" maxlength="6"  placeholder="请输入验证码"/><img class="verImg"></li><li class="item border-b Verify"><input type="text" class="the_input verifycode" maxlength="6"  placeholder="请输入短信验证码"/><a class="send_verify_code" id="send_verify_code_tel" href="javascript:;" rel="nofollow"><em>获取验证码</em></a></li><li class="send_verify_code_s" id="send_verify_code_tel_s" href="javascript:;" rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked/></span>7天内免登录</label></li><li class="li_btn"><a class="login-user-tel-btn"  />登录</a></li><li class="footer-link"><a href="javascript:;" rel="nofollow" class="tologin">账号密码登录</a></li></ul></form></div></div></div><div class="registered"></div></div><div class="panel_login animated" id="dialog_reg"><div class="panel_info"><i class="close_login">&times</i><div class="panel_tab"><div class="title"><div class="fl">手机号码注册</div><label class="fr register_text">已有账号？<a href="javascript:;" rel="nofollow" class="tologin">去登录</a></label></div><div class="clear"></div><div id="con_login_user_reg"><form action="" method="post"><ul><li class="item border-t userName"><input type="text" class="the_input topSpecial users_reg"  maxlength="11" placeholder="请输入手机号" /></li><li class="item checkVerimg" style=""><input type="text" class="the_input ver-img" maxlength="6"  placeholder="请输入验证码"/><img class="verImg"></li><li class="item border-c Verify"><input type="text" class="the_input verifycode" maxlength="6"  placeholder="请输入短信验证码"/><a class="send_verify_code" id="send_verify_code_reg" href="javascript:;" rel="nofollow"><em>获取验证码</em></a></li><li class="item border-b pwd"><input type="password" class="the_input password_reg" maxlength="20"  placeholder="请输入密码（最少8位，数字+字母）"/><em class="password-view"></em></li><li class="send_verify_code_s" id="send_verify_code_reg_s" href="javascript:;" rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox" name="read" value="1" class="read-protocol" checked/></span>我已阅读并同意</label><a class="toprotocol" href="//www.lianjia.com/zhuanti/protocol" target="_blank" >《链家用户使用协议》</a></li><li class="li_btn"><a class="register-user-btn"  />注册</a></li></ul></form></div></div></div><div class="registered"></div></div><div class="panel_login animated" id="dialog_forget"><div class="panel_info"><i class="close_login">&times</i><div class="panel_tab"><div class="title"><div class="fl">找回密码</div></div><div class="clear"></div><div id="con_forget_user_tel" class="con_forget_user_tel"><form action="" method="post"><ul><li class="item border-t userName"><input type="text" class="the_input topSpecial user_forget_phone" placeholder="请输入手机号"  maxlength="11" /></li><li class="item checkVerimg" style=""><input type="text" class="the_input ver-img" maxlength="6"  placeholder="请输入验证码"/><img class="verImg"></li><li class="item border-b Verify"><input type="text" class="the_input verifycode" maxlength="6"  placeholder="请输入短信验证码"/><a class="send_verify_code" id="send_verify_code_forget" href="javascript:;" rel="nofollow"><em>获取验证码</em></a></li><li class="item border-t pwd" style="margin-top:-1px;"><input type="password" class="the_input password_reg" maxlength="20"  placeholder="请输入密码（最少8位，数字+字母）"/><em class="password-view"></em></li><li class="send_verify_code_s" id="send_verify_code_forget_s"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_btn"><a class="user-forget"  />修改密码</a></li></ul></form></div><div id="con_forget_user_pw" class="con_forget_user_pw"><form action="" method="post"><ul><li class="item border-t pwd"><input type="password" class="the_input password_reg" maxlength="20"  placeholder="请输入密码（最少8位，数字+字母）"/><em class="password-view"></em></li><li class="show-error"><dd>用户名或密码错误</dd></li><li class="li_btn"><a class="modify-user-pswd"  />修改密码</a></li></ul></form></div></div></div><div class="registered"></div></div></div>
<!-- LianjiaIM Style --><link property='stylesheet' rel="stylesheet" href="https://s1.ljcdn.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css?_v=20181206222953"/><script src="//s1.ljcdn.com/web-im-sdk/static/1.1/lianjiaim1.1.min.js?v=20181207"></script><!-- <script src="//s1-ljcdn.test.lianjia.com:8400/web-im-sdk/static/1.1/lianjiaim1.1.min.js?v=20181207"></script> --><script>(function() {var imConf = {"ajaxroot":"\/\/ajax.api.lianjia.com\/","imAppid":"LIANJIA_WEB_20160624","imAppkey":"6dfdcee27d78b1107fceeca55d80b7bd"};let login = require('common/login');$.listener.on('userInfo', function (data) {if (data.code === 1) {data.ucid = '';}window.LJIM = new LianjiaIM({appid: imConf.imAppid,appkey: imConf.imAppkey,login: login.openLoginDialog,is_ljbb: true,userData: data,downAppUrl: '//www.lianjia.com/client/',appDesc: '立即下载链家APP，随时随地聊~',staticRoot: 'https://s1.ljcdn.com/feroot/?_v=20181206222953'})});})();</script><script type="text/javascript">var advert = 'https://s1.ljcdn.com/feroot/pc/asset/common/advert.js?_v=20181206222953';
    $.listener.on('userInfo', function (data) {
      window.loginData = data;
    });
    var mvl = document.createElement('script');
    mvl.type = 'text/javascript';
    mvl.async = true;
    mvl.src = advert;
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(mvl, s);
  </script><script type="text/javascript">(function(){var canonicalURL, curProtocol;var x=document.getElementsByTagName("link");if(x.length > 0){for (i=0;i<x.length;i++){if(x[i].rel.toLowerCase() == 'canonical' && x[i].href){canonicalURL=x[i].href;}}}if (!canonicalURL){curProtocol = window.location.protocol.split(':')[0];}else{curProtocol = canonicalURL.split(':')[0];}if (!canonicalURL) canonicalURL = window.location.href;(function() {var e = /([http|https]:\/\/[a-zA-Z0-9\_\.]+\.baidu\.com)/gi,r = canonicalURL,t = document.referrer;if (!e.test(r)) {var n = (String(curProtocol).toLowerCase() === 'https') ? "https://sp0.baidu.com/9_Q4simg2RQJ8t7jm9iCKT-xh_/s.gif" : "//api.share.baidu.com/s.gif";t ? (n += "?r=" + encodeURIComponent(document.referrer), r && (n += "&l=" + r)) : r && (n += "?l=" + r);var i = new Image;i.src = n}})(window);})();</script><!--cookie mapping--><img src='#' alt="cookie_mapping_url" style="display: none;"></body></html>
"""
response = etree.HTML(wb_data)
for quote in response.xpath('//div[@class="info-panel"]'):
    print quote.xpath('.//h2/a/text()')[0].strip().encode('utf-8')
    print quote.xpath('.//h2/a/@href')[0].strip().encode('utf-8')

    print quote.xpath('.//div[@class="col-1"]/div[@class="where"]/a/@href')[0].strip().encode('utf-8')
    print quote.xpath('.//div[@class="col-1"]/div[@class="where"]/a/span[@class="region"]/text()')[0].strip().encode(
        'utf-8')
    print quote.xpath('.//div[@class="col-1"]/div[@class="where"]/span[@class="zone"]/span/text()')[0].strip().encode(
        'utf-8')
    print quote.xpath('.//div[@class="col-1"]/div[@class="where"]/span[@class="meters"]/text()')[0].strip().encode(
        'utf-8')
    print quote.xpath('.//div[@class="col-1"]/div[@class="where"]/span[not(@class)]/text()')[0].strip().encode('utf-8')

    # other
    print quote.xpath('.//div[@class="col-1"]/div[@class="other"]/div[@class="con"]/a/@href')[0].strip().encode('utf-8')
    print quote.xpath('.//div[@class="col-1"]/div[@class="other"]/div[@class="con"]/a/text()')[0].strip().encode(
        'utf-8')
    print quote.xpath('.//div[@class="col-1"]/div[@class="other"]/div[@class="con"]/a/text()')[0].strip().encode(
        'utf-8')
    print quote.xpath('.//div[@class="col-1"]/div[@class="other"]/div[@class="con"]/text()')[0].strip().encode('utf-8')
    # chanquan
    print getList(quote.xpath('.//div[@class="chanquan"]/div[@class="fang-subway-ex"]/span/text()'))

    # col-3

    print quote.xpath('.//div[@class="col-3"]/div[@class="price"]/text()')[0].strip().encode('utf-8')
    print quote.xpath('.//div[@class="col-3"]/div[@class="price-pre"]/text()')[0].strip().encode('utf-8')

    # col -

    print getList(
        quote.xpath('.//div[@class="col-2"]/div[@class="square"]/div[not(@class)]/span[@class="num"]/text()')) + "人看房"

    print "***************************************************"


