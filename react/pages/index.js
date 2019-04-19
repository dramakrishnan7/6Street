import Link from 'next/link';
import Head from 'next/head';
import '../static/css/index.css';
import WordCloud from './wordcloud';

function Home() {
  
    return(
        
            <div className="Home">
            <Head>
                <title> Lyric Visualizer </title>
                <meta name="viewport" content="initial-scale=1.0, width=device-width" />
            </Head>
              <div className="ph9-l mw8 center">
                <main className="pa4 black-80 mb5">
                  <form className="sans-serif center pv6">
                    <fieldset id="sign_up" className="ba b--transparent ph0 mh0">
                      <legend className="f2 f1-ns fw8 green ph0 mh0 center">Search for a song, artist, genre or mood</legend>
                      <div className="cf mt4">
                      <input className="f6  fw8 f5-l input-reset bl bt br bb bw1 b--green fl black-80 bg-white pa3  w-100 w-75-m w-80-l br2-ns br--left-ns h-30" placeholder="Type your search here" type="text" name="email-address" id="email-address"/>
                      <input className="f6 fw8 f5-l button-reset fl pv3 tc bt bl br bb b--green bw1 bg-animate bg-green white pointer w-100 w-25-m w-20-l br2-ns br--right-ns h-30" type="submit" value="Search"/>
                      </div>                 
                    </fieldset>
                  </form>
                </main>
		<WordCloud />
              </div>
            </div>) ;
}



export default Home;
