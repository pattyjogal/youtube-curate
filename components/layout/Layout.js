import { PureComponent } from 'react';
import Head from "next/head";


const Layout = (props) =>  (
    <div>
    <Head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"
              integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4"
              crossorigin="anonymous"/>
    </Head>
    {props.children}
    </div>
);

export default Layout;
