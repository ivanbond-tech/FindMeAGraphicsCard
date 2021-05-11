<h2>FindMeAGraphicsCard</h2>
A simple python script that locates in-stock graphics cards at your closest MicroCenter and notifies you by text.
Requires a <a href='https://www.twilio.com'>Twilio</a> account (free trial available). Meant to be used in cronjob on a server or your local machine. Let me know if this helped you get a graphics card. Good luck!
<br>

<h4>Getting Started</h4>

<code>git clone https://github.com/ivanbond-tech/FindMeAGraphicsCard</code>

<h5>Creating a virtual environment</h5>
<code>pip install virtualenv</code><br>
<code>virtualenv venv</code><br>
<code>source venv/bin/activate</code><br>

<h5>Getting Twilio credentials</h5>
<p>Get your <code>ACCOUNT SID</code> and <code>AUTH TOKEN</code> and Twilio phone number from https://www.twilio.com/console</p>

<h5>Add your credentials</h5>

in <code>main.py</code>:
<ul>
  <li>change "account-SID" with your <code>ACCOUNT SID</code></li>
  <li>change "auth-token" with your <code>AUTH TOKEN</code></li>
  <li>change "recieving-phone" to <strong>your</strong> phone number with +country and area code
    <br><i>Example: +1987654321 (+1 for United States)</i></li>
  <li>change "sending-phone" to your Twilio account phone number</li>
  <li>change "store-id" to your specific MicroCenter store ID <br>
    <i>This can be found when visiting www.microcenter.com and looking in the url after <code>storeid=XXX</code> after setting your location (should be 3 digits)</i></li>
</ul>
  
<h5>Running the script</h5>
<code>python3 main.py</code>

<h5>Simple Cronjob Example</h5>
<code>sudo crontab -e</code><br>
<code>0 8 * * * /home/FindMeAGraphicsCard/main.py</code> 
<br><br>
<p><i>(This will schedule the script to run at 8 a.m. every day)</i></p>
