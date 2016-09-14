package testone;
import java.io.IOException;
import com.android.uiautomator.core.UiDevice;
import com.android.uiautomator.core.UiObject;
import com.android.uiautomator.core.UiObjectNotFoundException;
import com.android.uiautomator.core.UiSelector;
import com.android.uiautomator.testrunner.UiAutomatorTestCase;

public class testone extends UiAutomatorTestCase
{
    public void testDemo() throws IOException, UiObjectNotFoundException {
            
        // 启应用
        Runtime.getRuntime().exec("am start com.dx168.epmyg/com.dx168.epmyg.activity.SplashActivity");
        sleep(5000);
        
        // 点击抽屉图标
        UiObject locker = new UiObject(new UiSelector().resourceId("com.dx168.epmyg:id/btn_slide"));
        locker.click();
        sleep(2000);
        
        //点击【登录】按钮
        UiObject login = new UiObject(new UiSelector().resourceId("com.dx168.epmyg:id/btn_login"));
        login.click();
        sleep(2000);
        
        // 填写交易账号
        UiObject Mid_Account = new UiObject(new UiSelector().resourceId("com.dx168.epmyg:id/et_account"));
        Mid_Account.click();
        sleep(1000);
        Mid_Account.setText("166000000000002");
        sleep(1000);
        
        //填写密码
        UiObject Mid_Passwd = new UiObject(new UiSelector().resourceId("com.dx168.epmyg:id/et_pwd"));
        Mid_Passwd.click();
        sleep(1000);
        Mid_Passwd.setText("Aa111111" + "");
        sleep(5000);
        UiDevice.getInstance().pressBack();
        
        //点击【登录】按钮
        UiObject Press_login = new UiObject(new UiSelector().resourceId("com.dx168.epmyg:id/btn_submit"));
        Press_login.click();
        sleep(5000);
        
        //点击【开盘】text  防止出现侧边栏导致中断执行
        UiObject Press_Silver_Open = new UiObject(new UiSelector().resourceId("com.dx168.epmyg:id/tv_silver_open"));
        Press_Silver_Open.click();
        sleep(3000);
        
        //点击[粤贵银]
        UiObject Press_YGY = new UiObject(new UiSelector().resourceId("com.dx168.epmyg:id/tv_tab_01"));
        Press_YGY.click();
        sleep(3000);
        
        //点击[粤贵钯]
        UiObject Press_YGBA = new UiObject(new UiSelector().resourceId("com.dx168.epmyg:id/tv_tab_02"));
        Press_YGBA.click();
        sleep(3000);
        
        //点击[粤贵铂]
        UiObject Press_YGBO = new UiObject(new UiSelector().resourceId("com.dx168.epmyg:id/tv_tab_03"));
        Press_YGBO.click();
        sleep(3000);
        
        //点击[更多]
        UiObject Press_MORE = new UiObject(new UiSelector().resourceId("com.dx168.epmyg:id/tv_tab_05"));
        Press_MORE.click();
        sleep(3000);
        
        
        //再次点击首页抽屉图标
        locker.click();
        sleep(2000);
        
        //点击[设置]
        UiObject Press_SETTING = new UiObject(new UiSelector().resourceId("com.dx168.epmyg:id/ll_setting"));
        Press_SETTING.click();
        sleep(3000);
        
        //点击[退出登录]
        UiObject Press_LOGOUT = new UiObject(new UiSelector().resourceId("com.dx168.epmyg:id/tv_login_out"));
        Press_LOGOUT.click();
        sleep(3000);
        
        //再次点击【开盘】text  防止出现侧边栏导致中断执行
        Press_MORE.click();
        sleep(3000);
        
        //点击[粤贵银]
        Press_YGY.click();
        sleep(3000);
        
        //点击[粤贵钯]
        Press_YGBA.click();
        sleep(3000);
        
        //点击[粤贵铂]
        Press_YGBO.click();
        sleep(3000);
        
        //点击[粤贵银锭]
        UiObject Press_YGYD = new UiObject(new UiSelector().resourceId("com.dx168.epmyg:id/tv_tab_04"));
        Press_YGYD.click();
        sleep(3000);
        
        //点击[关闭]   关闭开户页面
        UiObject Press_Close = new UiObject(new UiSelector().resourceId("com.dx168.epmyg:id/rl_left"));
        Press_Close.click();
        sleep(3000);
        
        //点击[更多]
        Press_MORE.click();
        sleep(3000);
        
//        //点击【账号管理】按钮
//        UiObject obj_3 = new UiObject(new UiSelector().resourceId("com.tencent.mobileqq:id/account_switch"));
//        obj_3.click();
//        sleep(1000); 
  
//        // 点击菜单键
//        device.pressMenu();
//        sleep(1000);
//        
//        // 点击退出qq        
//        UiObject obj_4 = new UiObject(new UiSelector().text("退出QQ"));
//        obj_4.click();
//        sleep(1000);
//        
//        // 点击确定
//        UiObject obj_5 = new UiObject(new UiSelector().text("确定"));
//        obj_6.click();
    }
}